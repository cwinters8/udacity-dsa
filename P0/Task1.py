"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# helper function that appends to a list if item not in list already
def append(item, list: list):
    if item not in list:
        list.append(item)


# put nums in a list if they are not already in the list
nums = []
count = 0
for text in texts:
    append(text[0], nums)
    append(text[1], nums)

for call in calls:
    append(call[0], nums)
    append(call[1], nums)

# count numbers
print("There are", len(nums), "different telephone numbers in the records.")
