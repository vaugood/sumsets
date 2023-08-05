import os
import csv
import questionary
from itertools import chain, combinations
from pprint import pprint

dir = os.path.dirname(__file__)

predefined = []
required = []

target_sum = input("What is the sum of your missing expenses?\n$")
target_sum = float(target_sum)
limit = 6

data = []
required_list = []

with open(os.path.join(dir, dir, "transactions.csv")) as csvfile:
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        required_list.append(
            questionary.Choice(
                (
                    "$"
                    + str(row["amount"])
                    + " at "
                    + str(row["purchase"])
                    + " on "
                    + str(row["date"])
                ),
                value=index,
            )
        )
        data.append((row["date"], row["purchase"], float(row["amount"])))


def build_required(required_list, data):
    required_prompt = input(
        "Are there any expenses that must be included in the potential subset? Y/N "
    )
    if required_prompt.lower() == ("y"):
        required_index = questionary.checkbox(
            "Select required expense:", choices=required_list
        ).ask()
        for i in required_index:
            print(data[i])
            required.append(data[i])
        return required
    else:
        pass


def build_predefined(required):
    predefined = None
    predefined_prompt = input(
        "Are there any additional expenses you'd like to include? Y/N "
    )
    if predefined_prompt.lower() == ("y"):
        predefined_raw = input(
            'Enter additional expenses (separated by comma if applicable).\nExample: "13.37, 9.98, 11.11"\n-> '
        )
        predefined = predefined_raw.split(",")
        for index, i in enumerate(predefined):
            i = float(i.strip())
            data.append(("N/A", f"Custom Expense {index+1}", i))
            required.append(("N/A", f"Custom Expense {index+1}", i))
            print(f"Custom Exense {index+1}: ${i} added.")
    else:
        pass
    return required


def find_combinations(data, target_sum, limit, required):
    subsets = []
    # Generate all possible subsets of indices
    for r in range(len(data) + 1):
        for subset in combinations(data, r):
            subset_sum = sum(value for _, _, value in subset)
            if set(required).issubset(subset) and subset_sum == target_sum:
                # subset_values = [value for _, _, value in subset]
                subset_tuples = list(subset)
                # subsets.append((subset_values, subset_tuples))
                subsets.append(subset_tuples)
            if r > limit:
                break

    return subsets


build_required(required_list, data)
build_predefined(required)
subsets = find_combinations(data, target_sum, limit, predefined, required)

if subsets:
    print("Subsets found:")
    # for subset_values, subset_tuples in subsets:
    for subset_tuples in subsets:
        # print("Values:", subset_values)
        pprint(subset_tuples)
else:
    print("No subsets found.")
pprint(f"\n{data}")
