import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent_1 = meal_cost * tip_percent/100
    tax_percent_1 = meal_cost * tax_percent/100
    total_cost= meal_cost + tip_percent_1 + tax_percent_1
    print(round(total_cost))

    # Write your code here
meal_cost = float(input("enter meal cost").strip())
tip_percent = int(input("enter tip percent").strip())
tax_percent = int(input("enter tax percent").strip())

solve(meal_cost, tip_percent, tax_percent)
