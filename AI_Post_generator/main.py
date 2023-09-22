# sk-------------------------------------------
# ft:gpt-3.5-turbo-0613:personal::81R78YS1
# ftjob-3jzsFHJ2F2tG7EuAnpIVq7eR
# using an OpenAI API key

"""
========================================================================================================================
Made by: Alexandr  Pokorskiy

Project description:
    Task:
        - could you fine tune a Machine learning model using LinkedIns top influencers as data to help craft a great response to a customer?
Project made using the Streamlit and LLaMa AI
    Streamlit
        - https://streamlit.io/ Front end of the software, used for the creating a vibrant user interface that will be
            connecting directly to the AI Language model
    OpenAI - AI language model used for text communication with the user and recommending the right book sets based on the
        user's preferences and communication with the AI
        
    Research links:
        Top LinkedIn influencers : https://brigettehyacinth.com/top-20-most-followed-influencers-on-linkedin/
        Top influencers:
            1. Bill Gates	35.9 Million	USA
            2. Richard Branson	19.7 Million	UK
            3. Jeff Weiner	10.7 Million	USA
            4. Arianna Huffington	10.15 Million	USA
            5. Satya Nadella	10.06 Million	USA
            6. Mark Cuban	7.57 Million	USA
            7. Tony Robbins	7.24 Million	USA
            8. Melinda Gates	7.18 Million	USA
            9. Jack Welch	7.15 Million	USA
            10. Simon Sinek	6.31 Million	USA
            11. Deepak Chopra MD	5.81 Million	USA
            12. Daniel Goleman	5.70 Million	USA
            13. Justin Trudeau	5.43 Million	CAN
            14. Gary Vaynerchuk	5.26 Million	USA
            15. Adam Grant	4.87 Million	USA
        Note: I also added a couple of professional bios and posts from miscellaneous yet professional accounts from a few different LinkedIn users for a wider dataset outreach

        Fine-Tuning: https://platform.openai.com/docs/guides/fine-tuning/use-a-fine-tuned-model
========================================================================================================================
"""
import openai
import streamlit as st

st.set_page_config(
    page_title="Book recommender AI",
    page_icon="🧑‍💼",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a bug': "https://www.google.com",
        'About': "### This is a custom made AI helper built using OpenAI | Link: "}
)
st.title('Welcome Book Assistant AI!')
st.markdown('-----------------------------------------------------')

st.text("Made by Alex Pokorskiy")
st.text("Don't be afraid he doesn't bite! (or take over the world)")

key = open("api_key_holster.txt", "r").readline().strip('\n')
openai.api_key = key

# Fine-Tuning section can be found in fine_tuning.py

# Pre-prompt so that the AI does not misunderstand that he is the machine and needs to be responding as an assistant
pre = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
comp = openai.ChatCompletion.create(model="ft:gpt-3.5-turbo-0613:personal::81R78YS1", temperature=1,
                                    frequency_penalty=0, messages=[{"role": "system", "content": pre}])
# Stores the response of the as a string
ai_response = comp.choices[0].message.content

if "history" not in st.session_state:
    st.session_state.history = []

for history in st.session_state.history:
    with st.chat_message(history["role"]):
        st.markdown(history["content"])

# User input stored as string that will then be sent to the AI as a prompt
user_input = st.chat_input('Enter query')

if user_input:  # Must be true to start the process
    # User entry recorded
    with st.chat_message('user', avatar="human"):  # Name is user and avatar icon is human
        st.markdown(user_input)

    st.session_state.history.append({"role": "user", "content": user_input})
    # Store the AI response value in the rbt container

    # openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=<History>)
    comp = openai.ChatCompletion.create(model="ft:gpt-3.5-turbo-0613:personal::81R78YS1", temperature=1,
                                        frequency_penalty=0, messages=st.session_state.history)
    # Stores the response of the as a string
    ai_response = comp.choices[0].message.content

    with st.chat_message('assistant'):
        # Go through the items that the AI returns and stuff them into a string
        st.markdown(ai_response)  # Set it into the Message box

    # store the AI's reply
    st.session_state.history.append({"role": 'assistant', "content": ai_response})
