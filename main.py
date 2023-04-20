import numpy as np
import pandas as pd
import click

@click.command()
@click.option('--count', default=1)
def main(count):
    print(count)