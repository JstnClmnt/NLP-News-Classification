from nltk.corpus import stopwords

def remove_stop_words(s):
    s_cleaned=[]
    for w in s:
        if w.lower() not in stopwords.words("english") and len(w)>=3:
            s_cleaned.append(w)
 
    return s_cleaned