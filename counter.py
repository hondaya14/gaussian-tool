import collections


line = input().split()

counter = collections.Counter(line)

for c in counter.items():
    print(c)
