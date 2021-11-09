from tasks import Task_Manager
import click


@click.group()
def cli():
    pass
@click.command()
@click.argument('id', type=int)
@click.argument('name')
@click.argument('description')
def create_task(id, name, description):
    pass

@click.command()
def show_tasks():
    pass

cli.add_command(create_task)
cli.add_command(show_tasks)

if __name__ == '__main__':
    cli()