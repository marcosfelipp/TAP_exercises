word = input()

word = list(word)
vogal = ['a','e','i','o','u','A','E','I','O','U']

new_word = ''
for letter in word:
    if letter in vogal:
        new_word = new_word + 'ab' + letter
    else:
        new_word = new_word + letter

print(new_word)
