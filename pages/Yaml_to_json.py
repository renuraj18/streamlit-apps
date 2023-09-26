import streamlit as st
import yaml
import json
st.markdown("# Yaml to JSON coverter ❄️")
st.sidebar.markdown("# yaml to json converter  ❄️")


# Text area for entering YAML content
yaml_input = st.text_area("Enter YAML Content")

# Function to convert YAML to JSON
def convert_to_json(yaml_content):
    try:
        yaml_data = yaml.load(yaml_content, Loader=yaml.FullLoader)
        json_data = json.dumps(yaml_data, indent=4)
        return json_data
    except Exception as e:
        return f"Error: {str(e)}"

# Button to perform the conversion
if st.button("Convert"):
    if yaml_input:
        json_output = convert_to_json(yaml_input)
        st.code(json_output, language="json")
    else:
        st.warning("Please enter YAML content.")

# Explanation
st.write("Enter YAML content in the text area and click 'Convert' to convert it to JSON.")
