import streamlit as st
from groq import Groq

# Set up Groq API key
client = Groq(
    api_key=st.secrets["groq_api"],
)

st.title("Three Point Zero")

# Input from the user
user_input = st.text_area("Detail your experience with key numbers (if any)—like speed improvements or project metrics. Show us your impact!")

#Bullet Prompt Design
pre_prompt = """
You are an AI Assistant the follows instructions correctly.
Provide me with **three concise bulleted points** for an **ATS-friendly resume** based on the following work experience or project details. 
The bulleted points should adhere to these guidelines:
- **Highly professional tone**
- **Action-oriented sentences**
- **Emphasis on quantifiable achievements** (if applicable)
- **Concise** (maximum of 30 words per sentence)
- Identify and Incorporate **industry-specific keywords**

Here is my work experience details: <<<
"""

post_prompt = ">>> Please provide only the bulleted points without any additional information. Give each point on a seperate line."

def generate_bullets(prompt):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": pre_prompt+prompt+post_prompt,
        }
    ],
    model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Button to generate bullets
if st.button("Generate Bullets"):
    if user_input and len(user_input)>200:
        with st.spinner("Generating bullets..."):
            result = generate_bullets(user_input)
            st.subheader("Generated Content:")
            st.write(result)
    else:
        st.error("Please enter atleast 200 characters input before clicking the button.")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #333;
        color: #ff4500;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        Made with love by <a href="https://kartavyadesai.github.io/" target="Kartavya Desai">Kartavya</a>
    </div>
    """,
    unsafe_allow_html=True
)
