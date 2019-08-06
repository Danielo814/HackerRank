#!/usr/bin/python3
arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

left_to_right = 0
right_to_left = 0
for i in range(len(arr)):
    left_to_right += arr[i][i]
    right_to_left += arr[i][len(arr) - (i + 1)]

print(abs(left_to_right - right_to_left))
