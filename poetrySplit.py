from nltk.tokenize import sent_tokenize, word_tokenize
sader = "بَكَيْتُ حَتّى انْتَهَتَ الدّمُوْعُ"
ajoz = "صَلّيْتُ حَتّى ذَابَتِ الشّمُوْعُ"
baytPoetry = list(word_tokenize(sader+" "+ajoz))
#print(baytPoetry)

for word in baytPoetry:
    if(word == "هذه" or word="هَذِهِ" or word="هَذَهْ" word="هَذه" ):
        print("yes")

