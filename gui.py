import time
import PySimpleGUI as ps
import functions
import os

# filename = "todos.txt"

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as f:
        # f.writelines()
        pass
print("Done")
ps.theme('DarkRed')

label = ps.Text("Please type a TO-DO list")
clock = ps.Text('', key='clock')
input_box = ps.InputText(tooltip="Enter a TODO", key="todo")
# add_button = ps.Button(size=10, image_source='D:/Oops/GUI_INTERFACE/add.png', mouseover_colors='LightBlue2',
#                        tooltip='Add todo', key='Add ')
add_button = ps.Button("Add", size=10)
# list_box = ps.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
# list_box = ps.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
list_box = ps.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = ps.Button("Edit")
complete_button = ps.Button("Complete")
exit_button = ps.Button("Exit")

window = ps.Window("My TO-DO App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 25)
                   )

while True:
    event, key = window.read(timeout=10 )
    window['clock'].update(value=time.strftime("%a %b %d, %Y %H:%M:%S"))
    print(event)
    print(key)
    # print(key['todos'][0])
    todos = functions.get_todos()
    # print("not exit")
    # window.close()
    match event:
        case 'Add':
            value = key["todo"] + "\n"
            todos.append(value)
            functions.write_todos(todos_arg=todos)
            window['todos'].update(values = todos)

        case "Edit":
            try:
                todo_to_edit = key['todos'][0]  # to get only string from the list
                print(todo_to_edit)
                new_edit = key['todo']
                todoss = functions.get_todos()
                index = todoss.index(todo_to_edit)
                todoss[index] = new_edit
                functions.write_todos(todoss)
                window['todos'].update(values=todos)
            except IndexError:
                ps.popup("Select an item first", font=("Helvetica", 25))

        case "Complete":
            try:
                todo_to_complete = key['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                ps.popup("Select an item first", font=("Helvetica", 25))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=key['todos'][0])
        case ps.WIN_CLOSED:
            exit()
# window.close()

