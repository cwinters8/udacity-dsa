"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
durations_by_phone = {}
for call in calls:
    sender = call[0]
    receiver = call[1]
    duration = int(call[3])
    found_sender = False
    found_receiver = False
    for phone in durations_by_phone.keys():
        if sender == phone:
            durations_by_phone[sender] += duration
            found_sender = True
        if receiver == phone:
            durations_by_phone[receiver] += duration
            found_receiver = True
        if found_sender and found_receiver:
            break
    if not found_sender:
        durations_by_phone[sender] = duration
    if not found_receiver:
        durations_by_phone[receiver] = duration

longest = max(durations_by_phone, key=durations_by_phone.get)
print(
    longest,
    "spent the longest time,",
    durations_by_phone[longest],
    "seconds, on the phone during September 2016.",
)
