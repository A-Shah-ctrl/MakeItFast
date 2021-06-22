import nltk
from nltk.stem import PorterStemmer
import nltk.tokenize
from nltk.corpus import stopwords
from extract import Extract


WEBSITE = "https://www.cbc.ca/news/politics/trudeau-border-restrictions-coming-weeks-1.6075398"

def summarize(website: str):

    # Content of the website in text format
    content = Extract(website).get_content()

    #Separate the content into individual sentences
    sentences = nltk.sent_tokenize(content)

    #Separate the words in the content
    words = nltk.word_tokenize(content)
    ignore = set(stopwords.words("english"))
    base_stem = PorterStemmer()

    #Find frequencies of the words
    frequencies = {}
    for word in words:
        if word not in ignore:
            base = base_stem.stem(word)
            try:
                frequencies[base] += 1
            except KeyError:
                frequencies[base] = 1


    #Calculate the frequency of each sentence
    importance = {}
    length = len(sentences)
    overall = 0

    for i in range(length):
        total = 0
        num_words = 0
        for j in sentences[i]:
            base = base_stem.stem(j)
            try:
                total += frequencies[base]
                num_words += 1
            except KeyError:
                continue
        weight = total/num_words
        importance[i] = weight
        overall += weight

    cut_off = overall/length
    summary = ''
    for i in range(length):
        if importance[i] >= cut_off:
            summary += sentences[i]

    return summary

if __name__=="__main__":
    print(summarize(WEBSITE))

