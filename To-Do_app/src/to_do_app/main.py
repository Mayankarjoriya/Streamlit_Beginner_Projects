import streamlit as st

st.title("To-Do App")
st.sidebar.title("Recent To-Do's")

with st.container():
    st.text_input("Enter your To-Do's here")
    if st.button("Send balloons!"):
        st.balloons()
        To_do_column= st.columns(1,wrap=False)
        for i, col in enumerate(To_do_column,start=1):
            col.text("To-Do")





