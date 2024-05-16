import streamlit as st
from gurmukhiutils.converters.guru_latn import guru_latn
from gurmukhiutils.converters.guru_latn_pa import guru_latn_pa


# Function to initialize session state
def init_session_state():
    if 'input_data' not in st.session_state:
        st.session_state['input_data'] = ""
        st.session_state['guru_latn_result'] = ""
        st.session_state['guru_latn_pa_result'] = ""

# Call the function to initialize session state
init_session_state()

# Streamlit app interface
st.title('Generate IPA for Punjabi Language Using Gurmukhi Utils')

# Input from user
user_input = st.text_input('Enter Punjabi Word', st.session_state['input_data'])


# Button to process the input
if st.button('Generate IPA'):
    st.session_state['guru_latn_result'] = guru_latn(user_input)
    st.session_state['guru_latn_pa_result'] = guru_latn_pa(user_input)

result_container = st.container()
with result_container:
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"ShabadOS recommended result : {st.session_state['guru_latn_result']}")

    with col2:
        st.write(f"Latest Punjabi IPA  result : {st.session_state['guru_latn_pa_result']}")


