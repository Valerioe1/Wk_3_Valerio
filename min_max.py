
# Name: Edgar Valerio
# GiftHub Username: Valerioe1
# Date: 10/16/24
# Description: This program will prompt the use to say how many integers they would like and to type them out, and will say the max and min of the integers.

Integers = int((input("How many integers would you like to enter?")))
print("Please enter " + str(Integers) + " integers.")
count = 0
integer_list = []
while count < Integers :
    count += 1
    integer_list.append(int(input()))

print("Min:" + str((min(integer_list))))
print("Max:" + str((max(integer_list))))
