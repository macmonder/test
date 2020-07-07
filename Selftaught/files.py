myFile = []

with open("data.txt", "r") as file:
    myFile2 = [line.rstrip().split(";") for line in file]

with open("data.txt", "r") as file:
    for line in file:
        myFile.append(line.rstrip().split(';'))

print(myFile)
print(myFile2)
