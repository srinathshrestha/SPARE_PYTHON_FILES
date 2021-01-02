from collections import Counter
word = input('enter the word\n')
len_word = Counter(word)
for i,j in len_word.items() :
    if i !=' ':
        if j > 1:
            print(f'{i} is repeating {j} times')