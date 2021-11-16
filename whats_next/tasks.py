from datetime import date
from functools import total_ordering
from enum import Enum
import click


@total_ordering
class Task():

    priorities = Enum('Priority', 'Undefined Low Medium High')

    def __init__(self, id, name, description, priority='Undefined',
    conclusion_date="Undefined"):

        self.id = id
        self.name = name
        self.description = description
        self.set_priority(priority)
        self.creation_date = date.today().isoformat()
        self.conclusion_date = conclusion_date
        self.status = "Uninitialized"

    # needed for using task object as a key in a dictionary    
    def __hash__(self):
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

    def set_priority(self, priority):
        if priority != 'Undefined':
            for priority_name in Task.priorities:
                if priority == priority_name.name:
                    self.priority = priority_name
        else: 
            self.priority = Task.priorities.Undefined
    

    # sets the current status of a task
    def set_status(self, status):
        self.status = status


@click.command()
@click.argument('id', type=int)
@click.argument('name')
@click.argument('description')
@click.option('--priority', 
               default='Undefined', 
               type=click.Choice(['Undefined', 'Low', 'Medium', 'High'],
               case_sensitive=False))
def create_task(id, name, description, priority):
    new_task = Task(id, name, description, priority)
    return click.echo(new_task)

if __name__ == '__main__':
    create_task()