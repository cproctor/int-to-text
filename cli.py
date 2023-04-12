# cli.py
# ------
# Implements a simple number-to-text command-line interface.

from argparse import ArgumentParser
from int_to_text import int_under_10_to_text

parser = ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args()
text = int_under_10_to_text(args.number)
print(text)
