def count_vowels(input_str):
    
    input_str = input_str.lower()

    vowels = set("aeiou")

    vowel_count = sum(input_str.count(vowel) for vowel in vowels)

    return vowel_count
input_str = "My name is Victoria"
result = count_vowels(input_str)
print(result) 
