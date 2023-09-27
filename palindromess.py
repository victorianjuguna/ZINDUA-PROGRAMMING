with open ('words.txt','r')as file:
    for words in file:
        words= words.strip()
        if (words == words[::-1]):
            print (words)