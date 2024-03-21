import streamlit as st

# Define prompts and answers
prompts = ["Hi", "How are you?", "What's your name?"]
answers = ["Hello!", "I'm doing well, thanks for asking.", "My name is Chatbot."]

# Define function to match prompt and return answer
def generate_response(user_input):
    for i in range(len(prompts)):
        if user_input.lower() == prompts[i].lower():
            return answers[i]
    return "I'm sorry, I don't understand what you're trying to say."

# Define Streamlit app
def app():
    st.title("Simple Chatbot")
    st.write("Type a message and press Enter to chat with me.")
    user_input = st.text_input("Message:")
    if st.button("Send"):
        response = generate_response(user_input)
        st.text_area("Chatbot:", value=response)
        
if __name__ == '__main__':
    app()
