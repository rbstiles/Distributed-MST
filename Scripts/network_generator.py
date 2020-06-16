import sys

import click

@click.command()
@click.option('--count', default=6,
              help='Number of non-coordinator nodes.')
@click.option('--coordinator', default='coordinator',
              help='Name of coordinator.')
@click.option('--prefix', default='node',
              help='Prefix string of each node')
@click.option('--quiet', is_flag=True, help='Print to stdout')
def compose_generator(count: int, coordinator: str, prefix: str, quiet) -> str:
    """Generate the doc string."""
    main_template = """
    version: '3.3'
    services:
      server:
        build: node/.
        hostname: {coordinator}
        container_name: {coordinator}
        networks:
          - default
    {nodes}
    networks:
      default:
        driver: bridge
    """

    node_template = """
      {nodename}:
        build: node/.
        hostname: {nodename}
        container_name: {nodename}
        networks:
          - default"""

    assert count > 0

    nodes = ''.join([node_template.format(nodename=f"{prefix}{i}")
                     for i in range(count)])
    dockercompose = main_template.format(coordinator=coordinator, nodes=nodes)

    if not quiet:
        print(dockercompose, file=sys.stdout)

    return dockercompose


def network_config():
    """Create a dynamic network configuration."""
    pass


if __name__ == '__main__':
    compose_generator()