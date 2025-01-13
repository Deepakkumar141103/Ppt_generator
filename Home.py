import streamlit as st

def main():
    
    st.set_page_config(page_title="PDF to PowerPoint Generator", page_icon=":guardsman:", layout="wide")

    
    st.title("PDF to PowerPoint Generator")


    st.image("logo.jpeg", width=300)

    
    st.header("About the Project")
    st.write("""
        The **PDF to PowerPoint Generator** is a tool designed to automatically generate PowerPoint presentations from PDF documents.
        By analyzing and extracting key content from a given PDF, this tool helps create concise and visually engaging slides, 
        making it easier to prepare presentations quickly and efficiently.
    """)

    # Key features section
    st.header("Key Features")
    st.write("""
        - **Automatic Content Extraction**: The tool extracts key points and sections from the uploaded PDF.
        - **Engaging Slide Design**: Each slide is designed to be visually appealing and easy to follow.
        - **Customizable Topic Selection**: Choose a specific topic, and the tool will generate slides based on that topic.
        - **Saves Time**: With this tool, you don't have to manually copy-paste content into a PowerPoint.
    """)

    # Instructions on how to use the project
    st.header("How to Use the Tool")
    st.write("""
        1. **Upload a PDF**: Choose a PDF document that you'd like to convert into a PowerPoint presentation.
        2. **Select a Topic**: Pick a specific topic from the document to generate the slides.
        3. **Download the PowerPoint**: Once the slides are generated, download the PowerPoint file.
    """)

    
    
    

    
    st.markdown("""
    ---
    Created with ❤️ by our team !!!
    """)

if __name__ == "__main__":
    main()
