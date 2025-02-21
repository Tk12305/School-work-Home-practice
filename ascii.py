print("Extended ASCII")
count = 0
for i in range(257):
    base2=bin(i)
    for x in range(9):
        "0" + base2
    count += 1
    if count == 3:
        print()
        count = 0
    print("Character:", chr(i), "ASCII value:", i, "Binary value:", base2[2:], end="  ¦  ")
