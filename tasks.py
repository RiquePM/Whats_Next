from datetime import date
from functools import total_ordering

@total_ordering
class Task():

    priorities = {"None": 0, "Low": 1, "Medium": 2, "High": 3}
    
    def __init__(self, id, name, description, priority="None", conclusion_date=None):
        self.id = id
        self.name = name
        self.description = description 
        # Priorities: High // Medium // Low
        self.priority = Task.priorities.get(priority)
        self.creation_date = date.today()
        self.conclusion_date = conclusion_date
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
        return self.priority > other.priority
    
    # string representation of a task 
    # easy way to recreate object
    def __repr__(self):
        return "Task({}, '{}', '{}', '{}', {})".format(self.id, self.name, 
                                                       self.description,
                                                       self.priority,
                                                       self.conclusion_date
                                                       )

    # string representation of a task (end user)
    def __str__(self):
        pass

    # needs __lt__()
    def sort_by_priority(self,):
        pass
    
    # doesn't need __lt__() and __eq__()
    def sort_by_creation_date(self,):
        pass
    
    # needs __lt__()
    def sort_by_status(self,):
        pass
    
    # {task.name: [sub_task1, subt_task2]}
    # for ordering purposes 
    def sub_tasks_collection():
        pass

    # sets the current status of a task
    def set_status():
        pass

# may noat be necessary
class Sub_Task(Task):
    pass


class Task_Manager():
    # instantiate a task object (command-line argument)
    # save the object in a database
    def create_task():
        '''selects the id column of the database and 
           instanciate a new task object with the
           last id in the table incremented by one.
        '''
        id = None
        pass
    
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