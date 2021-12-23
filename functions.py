def position_in_alphabet(letter):
    integer_positions = [i for i in range(1,27)]
    letters_in_alphabet = [chr(i) for i in range(65,91)]
    combined = dict(zip(integer_positions, letters_in_alphabet))
    return [key for key in combined.items() if key[1] == letter.upper()][0][0]

def multiple_to_single_value(value):
    if len(str(value)) == 1:
        return value
    output = sum([int(a) for a in str(value)])
    if len(str(output)) > 1:
        return multiple_to_single_value(output)
    return output

def word_value(WORD):
    input = list(WORD)
    intermediate = sum([position_in_alphabet(i) for i in input])
    output = multiple_to_single_value(intermediate)
    return output

print(word_value('test'))