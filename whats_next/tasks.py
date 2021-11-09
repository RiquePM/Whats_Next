from datetime import date
from functools import total_ordering
from enum import Enum

@total_ordering
class Task():

    priorities = Enum('Priority', 'Undefined Low Medium High')

    def __init__(self, id, name, description, priority=priorities.Undefined,
    conclusion_date="Undefined"):
        
        self.id = id
        self.name = name
        self.description = description 
        self.priority = priority
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
    def __ge__(self, other):
        return self.priority.value >= other.priority.value
    
     
    # easy way to recreate a task object
    def __repr__(self):
        return "Task({}, '{}', '{}', '{}', {})".format(self.id, self.name, 
                                                       self.description,
                                                       self.priority.name,
                                                       self.conclusion_date
                                                       )

    # string representation of a task (end user)
    def __str__(self):
        return (
            f"{self.name:^20} | "
            f"{self.description:^40} | "
            f"{self.priority.name:^9} | "
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

