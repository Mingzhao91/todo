while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            print(f"{index + 1}-{todo}".rstrip())
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    elif user_action.startswith("complete"):
        # number = int(input("Number of the todo to complete: "))
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_to_remove = todos.pop(number - 1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove.rstrip()} was removed from the list"

        print(message)
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered an unknown command")

print('Bye!')