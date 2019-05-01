from nltk.corpus import stopwords

def remove_stop_words(s):
    s_cleaned=[]
    f = open('tagalog_stop_words.csv','r')
    d = f.read()
    stop_words_filipino = d.split('\n')
    for w in s:
        if w.lower() not in stopwords.words("english") and len(w)>=3 and w.lower() not in stop_words_filipino:
            s_cleaned.append(w)
 
    return s_cleaned