"""A medical clinic assigns a token number to every patient who visits. The token number starts from 1 and it is
given based on the order of arrival, to the n patients who arrive. But, the receptionist accepts bribe and lets a
person k in first. The task is to print the token number and the patient's name in the order in which they see the
doctor.
"""

all_ids = 'abcdefghijklmnopqrstuvwxyz'
queue = []
number_of_patients = int(input("How many patients? "))

for i in range(number_of_patients):
    token_id = (i + 1, all_ids[i])
    queue.append(token_id)

print('\nHere is the queue to start:')
for p in queue:
    print(p)

briber = input("\nWhich patient offers bribe? (Enter the letter) ")
briber_index = -1

for i in range(number_of_patients):
    print(queue[i])
    if briber in queue[i]:
        briber_index = i
        break

if briber_index > -1:
    new_queue = [queue[briber_index]]
    for i in range(1, len(queue) + 1):
        if queue[i - 1] != new_queue[0]:
            new_queue.append(queue[i - 1])
else:
    new_queue = queue

print('\nHere is the queue now:')
for p in new_queue:
    print(p)
