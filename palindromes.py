# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Open the input file for reading
with open("words.txt", "w") as input_file:
    words = input_file.read().split()

# Find palindromes in the list of words
palindromes = [word for word in words if is_palindrome(word)]

# Open the output file for writing
with open("palindromes.txt", "w") as output_file:
    for palindrome in palindromes:
        output_file.write(palindrome + "\n")

print("Palindromes have been written to palindromes.txt")
