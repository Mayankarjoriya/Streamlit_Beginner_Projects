import streamlit as st
import pandas as pd

st.title("To-Do App")

memo= st.session_state

# This is gonna save data of To-Do's
chart_list = [[None,None]]
dataframe_list = pd.DataFrame(chart_list,columns=('Name Of Task', 'Due Date'))


with st.container():

        task=st.text_input("Enter your task name...")
        due_date=st.datetime_input(
            "Enter your due date",

        )
        if st.button("Add Task"):
            if chart_list[0] == None:
                chart_list[0] = [task, due_date]
            elif chart_list[0] != None:
                dataframe_list.loc[len(dataframe_list)] = [task, due_date]
            data_widget = st.dataframe(dataframe_list)

        # if st.button("Send balloons!"):
        #     st.balloons()

st.write(memo)








with st.sidebar.title("To-Do's"):

    ALL_todo, pending_todo, complete_todo = st.tabs(["All Task", "Pending Task", "Complete Task"])
    with ALL_todo:
        st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    with pending_todo:
        st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with complete_todo:
        st.checkbox("Show gridlines")



