#!/usr/bin/env python
# encoding: utf-8

"""
A sample program to read a CSV file.
This program works for both Python 2/3.
"""

from __future__ import print_function
from __future__ import unicode_literals
import argparse
import csv
import io

import six


parser = argparse.ArgumentParser()
parser.add_argument("csv_file_path")
parser.add_argument("--encoding", default="utf_8")
options = parser.parse_args()

csv_reader = csv.reader(
    io.open(options.csv_file_path, "r", encoding=options.encoding),
    delimiter=",",
    quotechar='"'
)

print("--- header ---\n{}\n".format(six.next(csv_reader)))
print("--- data ---")
for row in csv_reader:
    print(row)
