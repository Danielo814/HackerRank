#!/usr/bin/python3
arr = [4, 4, 3, 1]
tallest = max(arr)
how_many = [num for num in arr if num == tallest]
return len(how_many)