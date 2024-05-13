def anagram (text_1, text_2):
    text_1 = text_1.lower()
    text_2 = text_2.lower()
    for i in text_1:
        index = text_2.find(i)
        if index == -1:
            return False
        else:
            text_2 = text_2.replace(i,'',1)
    return True

text_1 = input("First text: ")
text_2 = input("Second text: " )

if anagram(text_1, text_2)==True:
    print("Anagrams")
else:
    print ("Not anagrams")