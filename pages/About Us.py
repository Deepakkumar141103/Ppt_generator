import streamlit as st


# Add custom CSS to change the background color of the page
st.markdown(
    """
    <style>
    /* Set background color for the entire page */
    body {
        background-color: #f0f8ff;  /* Light blue background */
    }
    
    /* Optional: Modify text colors and header styles */
    h1 {
        color: #4B0082;  /* Indigo color for title */
    }

    h2 {
        color: #8A2BE2;  /* Blueviolet color for subheaders */
    }
    
    p, li {
        color: #333333;  /* Dark gray text for paragraphs and list items */
    }
    </style>
    """, unsafe_allow_html=True)

# Set the title of the app


# Add some description
st.header("Welcome to Our Platform!")
st.write("""
    We are a group of passionate developers who build innovative applications to solve real-world problems.
    Our goal is to create intuitive, powerful, and user-friendly solutions that help businesses thrive in today's digital world.
""")

# Add some team member information
st.subheader("Meet the Team")

st.write("""
- **KUNDAN KUMAR**: Co-Founder & CEO  
  Kundan leads the team with a passion for technology and innovation. He has a background in Computer Science and experience in Machine Learning.

- **DEEPAK KUMAR**: Co-Founder  
  Deepak specializes in backend development and Large Language Models (LLMs). He ensures that our products are robust and scalable.

- **TANUJA RAUTELA**: Hiring Recruiter (HR)  
  Tanuja specializes in backend development and image generation.

- **ADITI BHATT**: Manager  
  Aditi brings a creative touch to our projects, designing intuitive user interfaces that delight our customers.
""")

# Add a contact section
st.subheader("Contact Us")

st.write("""
If you have any questions or want to get in touch with us, feel free to reach out:
- Email: [singhdeepak141103@gmail.com](mailto:singhdeepak141103@gmail.com)
- Email: [rautelatanuja83@gmail.com](mailto:rautelatanuja83@gmail.com)
- Phone: (+91) 6396674381
- Phone: (+91) 7091014203
""")
