def is_vowel(letter):
    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        return True
    else:
        return False
    
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1      
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score