"""
Simple Todo Manager
A basic todo list manager with add, remove, and list functionality.
"""

class TodoManager:
    """A simple todo list manager."""
    
    def __init__(self):
        """Initialize an empty todo list."""
        self.tasks = []
    
    def add_task(self, task):
        """
        Add a new task to the todo list.
        
        Args:
            task (str): The task description to add
        """
        if task and task.strip():
            self.tasks.append(task.strip())
            print(f"✓ Added task: '{task.strip()}'")
        else:
            print("Error: Cannot add an empty task")
    
    def remove_task(self, task_index):
        """
        Remove a task from the todo list by index.
        
        Args:
            task_index (int): The index of the task to remove (1-based)
        """
        try:
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                print(f"✗ Removed task: '{removed_task}'")
            else:
                print(f"Error: Task index {task_index} is out of range")
        except (ValueError, TypeError):
            print("Error: Invalid task index")
    
    def list_tasks(self):
        """Display all tasks in the todo list."""
        if not self.tasks:
            print("\n📋 Todo List is empty!")
        else:
            print(f"\n📋 Todo List ({len(self.tasks)} task{'s' if len(self.tasks) != 1 else ''}):")
            print("-" * 40)
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("-" * 40)


def demo():
    """Demonstrate the Todo Manager functionality."""
    print("=== Todo Manager Demo ===\n")
    
    # Create a new todo manager
    todo = TodoManager()
    
    # Show initial empty list
    print("Initial state:")
    todo.list_tasks()
    
    # Add 3 tasks
    print("\nAdding tasks:")
    todo.add_task("Complete Python assignment")
    todo.add_task("Read documentation for new framework")
    todo.add_task("Prepare presentation slides")
    
    # List all tasks
    print("\nCurrent tasks:")
    todo.list_tasks()
    
    # Remove the second task
    print("\nRemoving task #2:")
    todo.remove_task(2)
    
    # List tasks again to show the change
    print("\nUpdated tasks:")
    todo.list_tasks()
    
    # Demonstrate error handling
    print("\nDemonstrating error handling:")
    todo.add_task("")  # Try to add empty task
    todo.remove_task(10)  # Try to remove non-existent task
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    demo()