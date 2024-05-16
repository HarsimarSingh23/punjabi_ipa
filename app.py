import streamlit as st
import random as r

# Function to initialize session state
def init_session_state():
    if 'input_data' not in st.session_state:
        st.session_state['input_data'] = ""

# Call the function to initialize session state
init_session_state()

# Streamlit app interface
st.title('Generate random number of input sequence')

# Input from user
user_input = st.text_input('Enter length', st.session_state['input_data'])


# Button to process the input
if st.button('Process Input'):
    number = r.randint(10 * user_input, (10 * user_input + 1 ) - 1  )
    st.write(f'Processed Data: {user_input.upper()}')  # Example processing

