import numpy as np
import pandas as pd
import click
from loguru import logger

@click.command()
@click.option('--count', default=1)
def main(count):
    print(count)

print ("Test_click")

print("logger imported")
