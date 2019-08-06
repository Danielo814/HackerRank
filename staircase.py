#!/usr/bin/python3
n = 25
for i in range(n):
    spaces = " " * (n - (i + 1))
    chars = "#" * (i + 1)
    print(spaces + chars)
