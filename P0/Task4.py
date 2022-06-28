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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = []

call_senders = set()
call_receivers = set()
text_numbers = set()

for call in calls:
    call_senders.add(call[0])
    call_receivers.add(call[1])

for text in texts:
    text_numbers.add(text[0])
    text_numbers.add(text[1])

for sender in call_senders:
    if sender not in call_receivers and sender not in text_numbers:
        possible_telemarketers.append(sender)

possible_telemarketers.sort()
print("These numbers could be telemarketers:")
for num in possible_telemarketers:
    print(num)
