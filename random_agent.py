import random
from vm import mvm

"""
operations = [1,1,7] # write your program in this list and DO NOT CHANGE ANYTHING

playground = mvm()
outputs = []
for _ in range(8):
    for i in operations:
        playground.operations[i]()
    outputs.append(playground.output())

print(outputs)
"""

# something weird with [4, 2, 0, 3, 0, 2, 0]
# so is operations = [0, 0, 7, 1]
# 6, 7 is fibonacci-ish generator
# 4, 6 power of 2 and 4, 6, 6 power of 3 and like [4] + [6] * n is power of n
# [0, 7, 1] -1, 1, -1, 1, -1, 1

def do():
    op = []
    for _ in range(16):
        op.append(random.randint(-1, 7))
    playground = mvm()
    return (playground.run(op))
