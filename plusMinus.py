#!/usr/bin/python3

arr = [1, 1, 0, -1, -1]
arr_length = len(arr)
positive = [pos for pos in arr if pos > 0]
negative = [neg for neg in arr if neg < 0]
number_positive = len(positive)
number_negative = len(negative)
number_zero = arr_length - (number_positive + number_negative)
print('{:7.6f}'.format(number_positive/arr_length))
print('{:7.6f}'.format(number_negative/arr_length))
print('{:7.6f}'.format(number_zero/arr_length))
