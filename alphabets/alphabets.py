import alpha
memo = {}
alphabets = alpha.Alphabets()
word = input("Enter a word: ")
for i in word:
    if i != ' ':
        memo[i] = getattr(alphabets, i).split('\n')

for i in range(15):
    a = ''
    for j in word:
        if j == ' ':
            a += "$$$$$$$$$$$$$$$$$$$$$$$$"
            continue
        else:
            a += memo[j][i]
    print(a)