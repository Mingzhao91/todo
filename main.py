from modules.functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, todo in enumerate(todos):
            print(f"{index + 1}-{todo}".rstrip())

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos.pop(number - 1)
            write_todos(todos)
            message = f"Todo {todo_to_remove.rstrip()} was removed from the list"

            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered an unknown command")

print('Bye!')
