import nltk
from nltk.stem import PorterStemmer
import nltk.tokenize
from nltk.corpus import stopwords
from extract_pdf import Extractor
from extract import Extract
import math
import operator

def summarize(path: str, mode: int):

    if mode == 1:
        # Content of the pdf in text format
        content = Extractor(path).get_text()
    else:
        content = Extract(path).get_content()
    #Separate the content into individual sentences
    sentences = nltk.sent_tokenize(content)

    #Separate the words in the content
    words = nltk.word_tokenize(content)
    ignore = set(stopwords.words("english"))
    base_stem = PorterStemmer()

    #Find frequencies of the words
    frequencies = {}
    total_words = len(words)
    for word in words:
        if word not in ignore:
            base = base_stem.stem(word)
            try:
                frequencies[base] += 1
            except KeyError:
                frequencies[base] = 1

    #Calculating the probabilities of the words in the document
    probabilities = {}
    for f in frequencies:
        probabilities[f] = frequencies[f]/total_words

    importance = {}
    for i in range(len(sentences)):
        total = 0
        num_words = 0

        for j in sentences[i]:
            base = base_stem.stem(j)
            try:
                total += probabilities[base]
                num_words += 1
            except KeyError:
                continue
        weight = total / num_words
        importance[i] = weight

    rounds = int(math.sqrt(len(sentences)))
    text = ""
    for r in range(rounds):
        index = max(importance.items(), key = lambda x : x[1])
        text += sentences[index[0]]
        importance.pop(index[0])

    return text

if __name__=="__main__":
    print("Welcome to MakeItFast. This is a basic extraction summarizer that is capable of summarizinga "
          "Wikipedia page and contents of a pdf file.")
    mode = int(input("Press 0 for Wikipedia Article\nPress 1 for a PDF\nYour preference: "))
    path = str(input("Enter the path of the PDF or the url of the website: "))
    print("============= ARTICLE SUMMARY =============\n\n\n")
    print(summarize(path,mode))

