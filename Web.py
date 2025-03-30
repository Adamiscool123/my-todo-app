import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']+"\n"
    todos.append(todo)
    functions.get_now(todos)



st.title("My Todo App")
st.subheader("This is my todo app")
st.write('This app increases your productivity')

for values, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(values)
        functions.get_now(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder='Add new todo...',
              on_change=add_todo,
              key='new_todo')




