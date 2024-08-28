"""Chapter 8 examples."""

def odd(n: int) -> bool:
    """Determines if ``n`` is odd.

    :param n: value to test
    :returns: True of ``n`` is odd.

    >>> odd(1)
    True
    >>> odd(2)
    False
    """
    return n % 2 == 1

import click
import sys

@click.command()
@click.argument('value', type=click.INT)
def main(value):
    if odd(value):
        click.echo(f"odd: {value}")
    else:
        sys.exit(f"even: {value}")

if __name__ == "__main__":
    main()
