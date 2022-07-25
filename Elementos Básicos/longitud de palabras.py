def get_word(sentence, n):
    # only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # only proceed if n is not more than the number of words in the sentence
        if n <= len(words):
            return (words[n - 1])
    return ("")


print(get_word("This a lesson about lists", 4))  # returns "lesson"
print(get_word("This a lesson about lists", -4))  # returns ""
print(get_word("Now we are cooking!", 1))  # returns "Now"
