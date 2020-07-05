
numbers = [1,2,3,4]

while True:
    inpt = input()
    if inpt == 'e':
        break
    else:
        if int(inpt) not in numbers:
            print('no')
        else:
            print('yes')
            break