import streamlit as st

st.title("To-Do App")

memo= st.session_state



with st.container():
    to_do_Name=st.text_input("Enter your task name...", key="task_name")
    due_date = st.datetime_input(
        "Enter your due date",
        key="due_date",
    )
    name_col, due_col = st.columns(2)
    name_col.write("Name")
    due_col.write("Due Date")
    tasks=[]
    for task in memo['task_name']:
        tasks.append(task)
    if st.button("Send balloons!"):
        st.balloons()

st.write(memo)








with st.sidebar.title("To-Do's"):

    ALL_todo, pending_todo, complete_todo = st.tabs(["All Task", "Pending Task", "Complete Task"])
    with ALL_todo:
        st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    with pending_todo:
        st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with complete_todo:
        st.checkbox("Show gridlines")



