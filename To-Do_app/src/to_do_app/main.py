import streamlit as st
import pandas as pd

st.title("To-Do App")

memo= st.session_state

# This is gonna save data of To-Do's
chart_list = []
# dataframe_list = pd.DataFrame(chart_list,columns=('Name Of Task', 'Due Date'))


with st.container():

        task=st.text_input("Enter your task name...",value=None)
        due_date=st.datetime_input(
            "Enter your due date",
            value =None
        )
        if st.button("Add Task"):
        #         dataframe_list.loc[len(dataframe_list)] = [task, due_date]
                chart_list.append(task)

        # st.write(chart_list)
        # data_widget = st.dataframe(dataframe_list)

        # if st.button("Send balloons!"):
        #     st.balloons()

# col1,col2,col3 = st.columns(3)

# with col1:
#     st.header("Task")
#
# with col2:
#     st.header("Due Date")
#
# with col3:
#     # Checkbox
#     st.header("Task Done")
# st.write(memo)


 # 1. Initialize with explicit string headers instead of numeric keys
if "tasks_df" not in st.session_state:
    st.session_state.tasks_df = pd.DataFrame(columns=["Name of Task", "Due Date"])

# 2. When adding data, match those exact headers
# (Inside your add task button logic):
new_row = pd.DataFrame([{"Name of Task": task, "Due Date": due_date}])
st.session_state.tasks_df = pd.concat([st.session_state.tasks_df, new_row], ignore_index=True)

# 3. Render the DataFrame and hide the numeric row index
st.dataframe(st.session_state.tasks_df, hide_index=True)




with st.sidebar.title("To-Do's"):

    ALL_todo, pending_todo, complete_todo = st.tabs(["All Task", "Pending Task", "Complete Task"])
    with ALL_todo:
        st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    with pending_todo:
        st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with complete_todo:
        st.checkbox("Show gridlines")



