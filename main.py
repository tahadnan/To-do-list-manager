from task_manager.task_mannager_class import TaskManager

def main():
    def print_welcome_message():
        print("""
                ╔══════════════════════════════════════════════════════════════╗
                ║                 Welcome to TaskManager CLI!                  ║
                ║                                                              ║
                ║  Manage your tasks efficiently with simple commands.         ║
                ║  Type 'help' to see available commands or 'exit' to quit.    ║
                ║                                                              ║
                ║  Let's get productive!                                       ║
                ╚══════════════════════════════════════════════════════════════╝
             """)

    def print_help_message():
        print("""
                ╔══════════════════════════════════════════════════════════════╗
                ║                   TaskManager CLI Commands                   ║
                ╠══════════════════════════════════════════════════════════════╣
                ║ add <task1> | <task2> | ...   : Add one or more tasks        ║
                ║ remove <task>                 : Remove a task or tasks       ║
                ║ mark-as-done / mad            : Mark one or more tasks       ║
                ║                                 as completed                 ║
                ║ list-both / lb                : Show all tasks               ║
                ║ list-todo / ltd               : Show pending tasks           ║
                ║ list-done / ld                : Show completed tasks         ║
                ║ clear-todo / cltd             : Clear all pending tasks      ║
                ║ clear-done / cld              : Clear all completed tasks    ║
                ║ reset                         : Clear all tasks              ║
                ║ help                          : Show this help message       ║
                ║ exit                          : Exit the program             ║
                ╚══════════════════════════════════════════════════════════════╝

                Note: Use '|' to separate multiple tasks in 'add','remove' or 'mark-as-done / mad'   command.
             """)
    print_welcome_message()
    to_do_list = TaskManager()
    while True:
        try:
            command = input("task-manager > ").strip()

            if command.lower() == 'help':
                print_help_message()

            elif command.lower() == 'exit':
                print('Goodbye !')
                break

            elif command.lower().startswith('add'):
                tasks = [task.strip() for task in command[4:].split('|') if task.strip()]
                print(to_do_list.add_task(*tasks))

            elif command.lower().startswith('remove') :
                tasks_tobe_removed = [task.strip() for task in command[4:].split('|') if task.strip()]
                print(to_do_list.add_task(*tasks_tobe_removed))
                print(to_do_list.remove_task(command[7:]))

            elif command.lower().startswith('mark-as-done') or command.lower().startswith('mad'):
                if command.lower().startswith('mark-as-done'):
                    tasks_tobe_mad = [task.strip() for task in command[13:].split('|') if task.strip()]
                    print(to_do_list.task_done(*tasks_tobe_mad))
                elif command.lower().startswith('mad'):
                    tasks_tobe_mad = [task.strip() for task in command[4:].split('|') if task.strip()]
                    print(to_do_list.task_done(*tasks_tobe_mad))

            elif command.lower().startswith('list-both') or command.lower().startswith('lb'):
                print(to_do_list.current_state('both'))

            elif command.lower().startswith('list-todo') or command.lower().startswith('ltd'):
                print(to_do_list.current_state('to-do'))

            elif command.lower().startswith('list-done') or command.lower().startswith('ld') :
                print(to_do_list.current_state('done'))

            elif command.lower().startswith('clear-todo') or command.lower().startswith('cltd'):
                print(to_do_list.clear_todo_list())

            elif command.lower().startswith('clear-done') or command.lower().startswith('cld'):
                print(to_do_list.clear_done_list())

            elif command.lower().startswith('reset'):
                print(to_do_list.reset())

            else:
                print("Invalid option, try 'help' to get more info on how to use this CLI.")
        except KeyboardInterrupt and EOFError:
            print("Try exit next time.")
            break
if __name__ == '__main__':
    main()
