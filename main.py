class TaskManager:
    def __init__(self): #creating instance named 'self'
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print('Task added:', task)

    def display_tasks(self):
        if not self.tasks:
            print('No tasks.')
        else:
            print('Tasks to do:')
            for index, task in enumerate(self.tasks, start=1): # using for loop starting from 1 which loopes through the list "self.tasks"
                print(f'{index}. {task}')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)   #'pop' function is used to remove from a list.
            print('Task completed:', completed_task)
        else:
            print('Invalid task index.')

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1) # using '-1' as in python the list indexing starts from '0'
            print('Task deleted:', deleted_task)
        else:
            print('Invalid task index.')

    def load_tasks_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.tasks = [line.strip() for line in lines]
        except FileNotFoundError:
            print("File not found could not load tasks")


    def save_tasks_to_file(self,file_path):
        with open(file_path, 'w') as file:  # using 'open' which is a built-in python function to open a file.
            for task in self.tasks:         #'w' means opening the file in writing mode so that automatically a new file is created or if already the file exists the existing content is erased.
                file.write(task + '\n')     # adds the tasks in new line


def main():
    task_manager = TaskManager()

    while True:
        print('Menu:')
        print('1. Add a new task')
        print('2. Display tasks')
        print('3. Mark a task as completed')
        print('4. Delete a task')
        print('5. Load tasks from a file')
        print('6. Exit')


        choice = input('Enter your choice: ')

        if choice == '1':
            task_description = input('Enter task: ')
            task_manager.add_task(task_description)
        elif choice == '2':
            task_manager.display_tasks()
        elif choice == '3':
            task_index = int(input('Enter task index to mark as completed: '))
            task_manager.complete_task(task_index)
        elif choice == '4':
            task_index = int(input('Enter task index to delete: '))
            task_manager.delete_task(task_index)
        elif choice == '5':
            file_path = input('Enter file path: ')
            task_manager.load_tasks_from_file(file_path)
        elif choice == '6':
            default_file_path = 'tasks.txt'
            task_manager.save_tasks_to_file(default_file_path)
            print(f'Tasks saved to {default_file_path}. Exiting.')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
