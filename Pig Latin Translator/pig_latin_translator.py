new_words = []
# get sentence from User
original = input("Provide a sentence for a translation ").strip().lower()

# Split sentence into words
words = original.split()

# loop through words and convert to pig latin
for word in words:
    # If word starts with vowel, add "yay" to end of the word
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    # If the word starts with consonants, move the consonant part to the last and add "ay" to the end of the word
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        consonants_part = word[:vowel_pos]
        the_rest_part = word[vowel_pos:]
        new_word = the_rest_part + consonants_part + "ay"
        new_words.append(new_word)
output = " ".join(new_words)

print(output)
