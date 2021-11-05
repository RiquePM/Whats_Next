from datetime import date
from functools import total_ordering
from enum import Enum

@total_ordering
class Task():

    priority = Enum('Priority', 'Undefined Low Medium High')

    def __init__(self, id, name, description, priority=priority.Undefined,
    conclusion_date="Undefined"):
        
        self.id = id
        self.name = name
        self.description = description 
        # Priorities: Undefined // High // Medium // Low
        self.priority = priority.name
        self.creation_date = date.today().isoformat()
        self.conclusion_date = conclusion_date
        # Status: Uninitialized // In progress // Completed
        self.status = "Uninitialized"

    # needed for using task object as a key in a dictionary    
    def __hash__(self) -> int:
        return hash(repr(self))

    # needed for the hash() method
    def __eq__(self, other):
        return repr(self) == repr(other)

    # comparison method for sorting purposes
    # x > y calls x.__gt__(y)
    def __gt__(self, other):
        return self.priority.value > other.priority.value
    
     
    # easy way to recreate a task object
    def __repr__(self):
        return "Task({}, '{}', '{}', '{}', {})".format(self.id, self.name, 
                                                       self.description,
                                                       self.priority,
                                                       self.conclusion_date
                                                       )

    # string representation of a task (end user)
    def __str__(self):
        return (
            f"{self.name:^20} | "
            f"{self.description:^40} | "
            f"{self.priority:^9} | "
            f"{self.status:^13} | "
            f"{self.creation_date:^15} | "
            f"{self.conclusion_date:^15} |"
        )
    
    # {task.name: [sub_task1, subt_task2]}
    # for ordering purposes 
    def sub_tasks_collection(self):
        pass

    # sets the current status of a task
    def set_status(self, status):
        self.status = status

# may noat be necessary
class Sub_Task(Task):
    pass


class Task_Manager():
    # instantiate a task object (command-line argument)
    # save the object in a database
    '''selects the id column of the database and 
       instanciate a new task object with the
       last id in the table incremented by one.
       '''
    def create_task(id, name, description, priority=Task.priority.undefined, 
                    conclusion_date="Undefined"
                    ):
        #id = None
        new_task = Task(id, name, description, priority, conclusion_date)
    
    # command-line argument
    # update an existing task of the database
    # see implementations details on trello
    def modify_task():
        pass
    
    # command-line argument
    # delete a task from the database
    def delete_task():
        pass

    # command-line argument
    def sorting_tasks():
        pass
    
    # command-line argument
    def display_tasks():
        pass