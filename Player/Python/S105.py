numerals = [
        {'l': 'M', 'v': 1000},
        {'l': 'D', 'v': 500},
        {'l': 'C', 'v': 100},
        {'l': 'L', 'v': 50},
        {'l': 'X', 'v': 10},
        {'l': 'V', 'v': 5},
        {'l': 'I', 'v': 1},
    ]

def roman_to_arabic(number):
    index_by_letter = {}
    for index in xrange(len(numerals)):
        index_by_letter[numerals[index]['l']] = index

    result = 0
    previous_value = None
    for l in reversed(number):
        index = index_by_letter[l]
        value = numerals[index]['v']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value

    return result
        
print(roman_to_arabic(raw_input().upper()))
