import os.path
import re
import nltk
nltk.download('punkt',quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('pos_tag', quiet=True)
from nltk import pos_tag
nltk.download('wordnet', quiet=True)
from nltk.corpus import wordnet
nltk.download('word_tokenize')
from nltk.tokenize import word_tokenize
nltk.download('word_tokenize', quiet=True)
from nltk.corpus import stopwords
nltk.download('stopwords', quiet=True)
from nltk.stem import WordNetLemmatizer
nltk.download('WordNetLemmatizer', quiet=True)
import sys
import os

path=sys.argv[1]
path_1=sys.argv[2]

if not os.path.exists(path_1):
    os.makedirs(path_1)
    
wnl = WordNetLemmatizer()
# lemmatizer.lemmatize(i)
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
stopWords=["0","1","2","3","4","5","6","7","8","9","\'s","\'"]


shuliang=0
terms_1=[]  #tokens
m = 0
for parentdir, dirname, filenames in os.walk(path):
    for filename in filenames:
#         print(filename)
        if os.path.splitext(filename):
            m = m + 1
            tokens=[]
            with open(path+'/'+filename,'r',encoding="ISO-8859-1") as file:
                u=file.read()
                u = u.lower()
                result = re.sub(r'[~`@#$%^&*()_\-+=|\\{\}\[\]:;\"\<>,/·￥…（）—【】、《》，。]+', ' ', u)
                file.close()
            words = word_tokenize(result)
            
            for i in range(len(words)):
                xieru=wnl.lemmatize(words[i],get_wordnet_pos(pos_tag([words[i]])[0][1]))
                tokens.append(xieru)
            baocun=open(path_1+'/'+filename+".txt",'a')
            tokens_z=[]
            for i in tokens:
                panduan=1
                for z in stopWords:
                    if z in i:
                        panduan=0
                        break
                if panduan:
                    if len(i)>2:
                        if "." in i:
                            n=i.replace('.','')
                            tokens_z.append(n)
                        else:
                            tokens_z.append(i)
                    else:
                        tokens_z.append(i)
            terms_1.append(tokens_z)
            wenben=""
            for i in tokens_z:
                if i=="." or i=="!"or i=="?":
                    wenben=wenben+"."
                    baocun.write(wenben+"\n")
                    wenben=""
                else:
                    wenben=wenben+" "+i
            baocun.close()

print("Total number of documents: %d"%m)

wordcount = {}
for i in terms_1:
    for word in i:
        if word !=".":
            wordcount[word] = wordcount.get(word, 0)+1
print(f'Total number of tokens: {sum((wordcount.values()))}')
print(f"Total number of terms: {len(wordcount)} ")
