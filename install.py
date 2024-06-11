import os
import streamlit as st

def install_python():
    # Directory containing the markdown files
    directory = 'Install'
    # List all markdown files in the directory
    markdown_files = [f for f in os.listdir(directory) if f.endswith('.md')]
    # Streamlit application
    st.title('How to install Python')
    # Display the list of markdown files in a sidebar
    st.header("Select a Assignment")
    selected_file = st.selectbox('', markdown_files)
    # Display the content of the selected markdown file
    if selected_file:
        st.subheader(selected_file)
        file_path = os.path.join(directory, selected_file)
        with open(file_path, 'r') as file:
            markdown_content = file.read()
            st.markdown(markdown_content)
