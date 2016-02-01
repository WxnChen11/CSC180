import os
os.chdir("/u/a/chenw120/_Courses/csc180/labs/lab08")

f = open("data2.txt", encoding = "utf-8")

text = f.read()

print(text)

lines = text.split('\n')

for i in lines:
    
    temp = i.lower()
    
    if "lol" in temp:
        print (i)


#lol = text.find("lol")

#Problem 3

def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """
    
    keys = list(d.keys())
    values = list(d.values())
    
    res = ""
    
    for i in range (len(keys)):
        res += str(keys[i]) + ", " + str(values[i]) + "\n"
        
    return res
        

print("\n\n")
d = {"hi" : "hello", 12 : 14, "amy" : "joe" , "411" : "43"}

print(dict_to_str(d))

def dict_to_str_sorted(d):
    
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""
    
    keys = list(d.keys())
    values = list(d.values())
    
    pairs=[]
    
    for i in range(len(keys)):
        pairs += [(keys[i], values[i])]
    
    pairs = sorted(pairs)
    
    res=""
    
    for i in range(len(pairs)):
        res += str(pairs[i][0]) + "," + str(pairs[i][1]) + "\n"
    
    return res
    
d = {10 : 15, 12 : 14, 2 : 200 , 1520 : 610}

print(dict_to_str_sorted(d))
    
    
#Problem 5

def get_readability(s):
    
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    list_vowel_phones = ['aa', 'ae', 'ao', 'ay', 'ey', 'iy', 'oy']
    
    s = s.lower()
    
    syllables = 0
    
    for i in range(len(s)):
        if s[i] in list_vowels:
            syllables += 1
        elif s[i] == 'y':
            syllables += .5

    for z in range(len(s)):
        if s[i:i+2] in list_vowel_phones:
            syllables -= 1
    
    s = s.replace("!", ".")
    s= s.replace("?", ".")
            
    sentences = s.split(".")
    
    for k in sentences:
        if k == " " or k == "":
            sentences.remove(k)
    
    no_sentences = len(sentences)
    
    words = len(s.split())
    
    return 0.39 * (words/no_sentences) + 11.8 * (syllables/words) - 15.59


s = "hillo"

print(s[1:2])


s = "this is a sample sentence"

print(s.split())

s = s.replace("!", ".")
s= s.replace("?", ".")
            
sentences = s.split(".")

for k in sentences:
    if k == " " or k == "":
        sentences.remove(k)


print(s.split("."))
print(sentences)

f = open("lorem.txt", encoding = "utf-8")

text = f.read()

print(get_readability(text))








