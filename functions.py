FILEPATH = "todos.txt"
def get_todos(filepath = FILEPATH):
    """Read the text from file and return todo items"""
    with open(filepath, 'r') as filepath:
        todos_local = filepath.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Write the todos items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


    