import click

@click.command()
@click.option('--count', type=int, default=1)
@click.argument('name')
def hello(name, count):
    for i in range(count):
        click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()