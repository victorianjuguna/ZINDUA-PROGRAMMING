import string

def is_palindrome(input_str):
    cleaned_str = ''.join(char for char in input_str if char not in string.whitespace + string.punctuation).lower()
    
    return cleaned_str == cleaned_str[::-1]

input_str = "i did, did i"
result = is_palindrome(input_str)
print(result)
