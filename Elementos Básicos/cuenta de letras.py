def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


count_letters('aaaaa')
print(count_letters('aaaaa'))

count_letters("Tenant's")
print(count_letters("Tenant's"))

count_letters("a long string with a lot of letters in it")
print(count_letters("a long string with a lot of letters in it"))
