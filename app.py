import streamlit as st

def display_metadata(form_name, variables):
    st.success("Here is the metadata for your form:")
    st.write(f"**Name of the Form:** {form_name}")
    for var_name, var_details in variables.items():
        if isinstance(var_details, dict):  
            st.write(f"**{var_name}:** Range from {var_details['min']} to {var_details['max']}")
        else:  
            st.write(f"**{var_name}:** {var_details}")

def main():
    st.title("Let's create a personalized form!")
    st.write("Let's start with metadata.")

    form_name = st.text_input("Name of the Form (100 characters max)", max_chars=100)

    if "variables" not in st.session_state:
        st.session_state.variables = {}

    if form_name:
        st.write("### Add Variables to Your Form")
        variable_options = ["Description", "Age", "Weight", "Height"]
        selected_variable = st.selectbox("Choose a variable to add", variable_options)

        if selected_variable == "Description":
            description = st.text_area("Description (200 characters max)", max_chars=200)
            if st.button("Add Description"):
                st.session_state.variables["Description"] = description
                st.success("Description added!")

        elif selected_variable in ["Age", "Weight", "Height"]:
            min_value = st.number_input(f"Minimum {selected_variable}", value=0, step=1)
            max_value = st.number_input(f"Maximum {selected_variable}", value=100, step=1)
            if st.button(f"Add {selected_variable}"):
                st.session_state.variables[selected_variable] = {
                    "min": min_value,
                    "max": max_value,
                }
                st.success(f"{selected_variable} added!")

    if st.button("Submit"):
        if not form_name:
            st.error("Please provide a name for the form.")
        elif not st.session_state.variables:
            st.error("Please add at least one variable.")
        else:
            display_metadata(form_name, st.session_state.variables)

if __name__ == "__main__":
    main()
