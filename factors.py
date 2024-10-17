# Name: Edgar Valerio
# GiftHub Username: Valerioe1
# Date: 10/16/24
# Description: This will find the factors or any integer you enter.

integer = int(input( "Please enter a positive integer:" ))
print("The factors of " + str(integer) + " are: ")

for factor in range(1, integer + 1):
    if integer % factor == 0:
        print(factor)
