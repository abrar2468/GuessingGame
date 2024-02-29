import random
randomNumber = random.randrange(1,200)
#print(randomNumber)

userInput = int(input("guess the number:"))
if userInput > randomNumber:
    print(randomNumber)
    print("the number is to high")
elif randomNumber >userInput:
    print(randomNumber)
    print("the number is too low")

else:
    print(randomNumber)
    print("yes,you match the number")