# Valid Word
# Input:
# words = ["hEllo##", "This^^"]
# letters = ["h", "e", "l", "o", "t", "h", "s"]
# Output: 1
# Explaination: hEllo## is a valid word, This^^ is not a valid word (ignore symbol)

def valid_word(words, letters):
    result = 0
    for word in words:
        word = [c for c in word if c.isalpha()]
        count = 0
        for c in word:
            if c.lower() in letters:
                count += 1
        if count == len(word):
            result += 1
    return result


words = ["hEllo##", "Ths^^"]
letters = ["h", "e", "l", "o", "t", "h", "s"]
print(valid_word(words, letters))