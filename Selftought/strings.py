for letter in 'Camus':
    print(letter)

test = ' word'
test2 = "words{}".format(test)
print(test2)
print(test2.split(' '))
print('A screaming comes across the sky'.replace('s','$') )
print("Hemingway".find('m'))

quote = 'It was a bright cold day in April, and the clocks were striking thirteen.'
print(quote[:quote.index(',')])

var = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(''.join(var))

for i, word in enumerate(var):
    var[i] = word.upper()
    print(i)

print(var)
