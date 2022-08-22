def first_letters(inputLetters):
    first_letter = []
    for letter in inputLetters:
        try:
            assert type(letter) == str, f'{letter} not is on str'
            assert len(letter) > 0, 'not is permit str equal 0'

            first_letter.append(letter[0])
        except AssertionError as err:
            print(err)
    return first_letter


list_letters = []
list_letters2 = ['test']
list_letters3 = [3]
print(first_letters(list_letters))
print(first_letters(list_letters2))
print(first_letters(list_letters3))