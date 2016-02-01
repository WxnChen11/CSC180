#Problem 1

# import os
# os.chdir("/u/a/chenw120/_Courses/csc180/labs/lab09")
# 
# text = open("text.txt", encoding="utf-8").read().split()
# 
# 
# word_counts = {}
# 
# for words in text:
#     if words.lower() in list(word_counts.keys()):
#         word_counts[words.lower()] = word_counts[words.lower()] + 1
#     else:
#         word_counts[words.lower()] = 1
# 
# freq = {}
# 
# for keys in word_counts:
#     freq[word_counts[keys]] = keys
# 
# freq = sorted(freq.items())
# 
# while len(freq) > 10:
#     del freq[0]
# 
# print(freq)
# 
# 
# inv_freq = {6: "the", 12: "a", 1:"hi"}
# print(sorted(inv_freq.items()))
# 
# print(list(inv_freq.items()))
# 
# dict = {}
# 
# dict["key"] = 1
# dict["key"] = dict["key"] + 1
# print(dict)
# 
# del dict[list(dict.keys())[0]]

#Problem 2 - done in gedit

#Problem 3

# import urllib.request
# f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=computer+science&fr=yfp-t-917")
# page = f.read().decode("utf-8")
# f.close()
# print(page)
# 
# s = "hi my name is wenxin"
# print(s.split())

def return_terms(s):
    
    sp = s.split()
    url = "https://ca.search.yahoo.com/search?p="
    for w in range(len(sp)):
        if w + 1 == len(sp):
            url += sp[w]
        else:
            url += sp[w] + "+"

    f = urllib.request.urlopen(url)
    page = f.read().decode("utf-8")
    f.close()
    #print(page)
    
    index = page.rfind("results</span></div></div></li></ol></div></div>")
    
    num_res = ""
    
    while page[index] != ">":
        
        if page[index].isdigit():
            num_res += page[index]
            
        index -= 1
       
    res = ""
    
    for i in range(0,len(num_res),3):
        if i+3 < len(num_res):
            res += num_res[i:i+3] + " "
        else:
            res += num_res[i:]
    
    print("The search term: '%s' results in %s terms" % (s,res[::-1]))
    
    return int(num_res[::-1])

return_terms("computer science")


def choose_variant(variants):
    
    terms = []
    max_res = -1
    
    for phrase in variants:
        tempstr = '"' + phrase + '"'
        terms += [tempstr]
    
    for search in terms:
        res = return_terms(search)
        if res > max_res:
            max_res = res
            variant = search
    
    return variant

print(choose_variant(["five year anniversary","fifth anniversary"]))

print(choose_variant(["top ranked school university of toronto","top ranked school waterloo"]))

print(choose_variant(["Chris chan","Tony Kung"]))

        
        
        
        
        
        
        
        
        
        
        




