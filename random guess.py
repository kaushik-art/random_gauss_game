import random
import time
a = int(input("From\n"))
b = int(input("To\n"))
random_num = random.choice(range(a,b))
for choice in range(1,b):
    c = int(input("Enter guess number\n"))
    gauss_left = -(choice - b)
    print("Wait.....")
    time.sleep(2)
    print("guess left = ",gauss_left)
    if c == random_num:
        print("correct guess")
        print("you guess in ",choice)
        break
    else:
        print("Wrong choice")