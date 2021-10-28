def disemvowel(string_):
    vowels = 'aeiou'
    return_string = ''
    for letter in string_:
        if letter.lower() not in vowels:
            return_string += letter
    return return_string