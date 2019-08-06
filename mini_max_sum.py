#!/usr/bin/python3
arr = [1, 3, 5, 7, 9]
new_list = []
for x in range(len(arr)):
    new_list.append(sum(arr[:x] + arr[x+1:]))
print(min(new_list), max(new_list))
