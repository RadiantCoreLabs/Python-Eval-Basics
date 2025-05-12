successful = True
for number in range (5):
    print("Tried")
    if successful :
        print("Successful")
        break
else:
    print("Tried 5 times and failed")

successful = False
for number in range (5):
    print("Tried")
    if successful :
        print("Successful")
        break
else:
    print("Tried 5 times and failed")