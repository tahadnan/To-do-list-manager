from ttask_manager.ttask_manager import TaskManager
import os       
def main():
    def print_welcome_message():
        print("""
        ╔═══════════════════════════════════════════════════════════════════════════╗
        ║                                                                           ║
        ║   ████████╗ █████╗ ███████╗██╗  ██╗    ███╗   ███╗ █████╗ ███╗   ██╗      ║
        ║   ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔══██╗████╗  ██║      ║
        ║      ██║   ███████║███████╗█████╔╝     ██╔████╔██║███████║██╔██╗ ██║      ║
        ║      ██║   ██╔══██║╚════██║██╔═██╗     ██║╚██╔╝██║██╔══██║██║╚██╗██║      ║
        ║      ██║   ██║  ██║███████║██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║      ║
        ║      ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝      ║
        ║                                                                           ║
        ║              Welcome to TaskMan - Your Personal Task Manager!             ║
        ║                                                                           ║
        ║        Manage your tasks efficiently with simple CLI commands.            ║
        ║        Type 'help' to see available commands or 'exit' to quit.           ║
        ║                                                                           ║
        ║                     Let's boost your productivity!                        ║
        ╚═══════════════════════════════════════════════════════════════════════════╝
        """)

    def print_help_message():
        print("""
        ╔═══════════════════════════════════════════════════════════════════════════╗
        ║                         TaskMan CLI Commands                              ║
        ╠═══════════════════════════════════════════════════════════════════════════╣
        ║ add <task1> | <task2> | ...   : Add one or more tasks                     ║
        ║ remove <task1> | <task2> | ...: Remove one or more tasks                  ║
        ║ mark-as-done / mad <task1>... : Mark one or more tasks as completed       ║
        ║ list-both / lb                : Show all tasks (to-do and done)           ║
        ║ list-todo / ltd               : Show pending tasks                        ║
        ║ list-done / ld                : Show completed tasks                      ║
        ║ clear-todo / cltd             : Clear all pending tasks                   ║
        ║ clear-done / cld              : Clear all completed tasks                 ║
        ║ reset                         : Clear all tasks (both to-do and done)     ║
        ║ report [name]                 : Generate a report (optional custom name)  ║
        ║ save                          : Save current state to file                ║
        ║ help                          : Show this help message                    ║
        ║ clear                         : Clear the screen                          ║
        ║ exit                          : Exit the program                          ║
        ╠═══════════════════════════════════════════════════════════════════════════╣
        ║ Note: Use '|' to separate multiple tasks in 'add', 'remove', or 'mad'     ║
        ║       commands. Example: add buy groceries | call mom | finish report     ║
        ╚═══════════════════════════════════════════════════════════════════════════╝
        """)
    def clear_screen():
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For Mac and Linux
        else:
            _ = os.system('clear')
    
    print_welcome_message()
    to_do_list = TaskManager()
    pyfile_path = os.path.dirname(os.path.realpath(__file__))
    json_data_file = os.path.join(pyfile_path, 'data.json')
    print(to_do_list.load_recent_state(json_data_file))
    while True:
        try:
            command = input("task-manager > ").strip()            
            if not command:
                print("Invalid option,the input cannot be blank,try 'help' to get more info on how to use this CLI.")

            elif command.lower() == 'clear' :
                clear_screen()
                continue

            elif command.lower() == 'help':
                print_help_message()

            elif command.lower() == 'exit':
                save = input("Wanna save the current state [Y/n]: ")
                if save.lower() == 'y' or save.lower() == 'yes':
                    print(to_do_list.save_current_state(json_data_file))
                    break
                else:
                    print('Data not saved.')
                    break
            elif command.lower() == 'save':
                print(to_do_list.save_current_state(json_data_file))

            elif command.lower().startswith('add'):
                tasks = [task.strip() for task in command[4:].split('|') if task.strip()]
                print(to_do_list.add_task(*tasks))

            elif command.lower().startswith('remove') :
                tasks_tobe_removed = [task.strip() for task in command[7:].split('|') if task.strip()]
                print(to_do_list.remove_task(*tasks_tobe_removed))

            elif command.lower().startswith('mark-as-done') or command.lower().startswith('mad'):
                tasks_tobe_mad = [task.strip() for task in command.split(maxsplit=1)[1].split('|') if task.strip()]
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

            elif command.lower().startswith('report'):
                report_name = command[len('report'):].strip()
                if report_name and '\n' not in report_name:
                    print(to_do_list.report(pyfile_path,f"{report_name}.txt"))
                else:
                    print(to_do_list.report(pyfile_path))

            elif command.lower().startswith('reset'):
                print(to_do_list.reset())
            else:
                print("Invalid option, try 'help' to get more info on how to use this CLI.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected.Exiting... ")
            save = input("Wanna save the current state [Y/n]: ")
            if save.lower() == 'y' or save.lower() == 'yes':
                print(to_do_list.save_current_state())
                break
            else:
                print('Data not saved.')    
                break
            
        except EOFError:
            print("\nEOF detected. Exiting...")
            save = input("Wanna save the current state [Y/n]: ")
            if save.lower() == 'y' or save.lower() == 'yes':
                print(to_do_list.save_current_state())
                break
            else:
                print('Data not saved.')    
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again or type 'help' to see available commands or 'exit' to quit.")

    print("Thank you for using TaskManager CLI. Goodbye!")
if __name__ == '__main__':
    main()
