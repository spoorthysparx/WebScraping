import re
import string
from collections import Counter
top_n=5
new_stopwords = []

def get_statistics(data):
"""it is the main function which calls all the functions and returns to the main program
param data:contents of the page"""
    lines=get_lines(data)
    words=get_words(lines)
    unique_words=list(set(words))
    cleaned_words = read_file()
    top_n_words=get_top_n_words(words,top_n,cleaned_words)
    statistics={"line_count":len(lines),"word_count":len(words),"unique_words":len(unique_words),"top_words":top_n_words}
    return statistics

def get_lines(data):
"""gets contents of the page and splits into individual lines
param data: content of the page"""
    lines=[]
    for para in data:
        lines.extend(re.split("[.!?]+",para))    
    cleaned_lines=clean_string(lines)
    return cleaned_lines
    
def clean_string(lines):
    """gets the individual lines and makes it free from any punctuation marks
    param lines: individual lines of the content"""
    cleaned_lines=[]
    for line in lines:
        st=str.maketrans("","",string.punctuation)
        new_line=line.translate(st).lower().strip()
        if new_line:
            cleaned_lines.append(new_line)
    return cleaned_lines

def get_words(lines):
    """gets the lines and splits them into individual words
    param lines:individual lines in the content"""
    words=[]
    for line in lines:
        words.extend(line.split(" "))   
    return words    


def read_file():
    """reads the contents in file stopwords.txt
    param None"""
    with open('stopwords.txt','r') as f:
        stopwords=f.readlines()
        cleaned_words=get_cleaned_words(stopwords)
        return cleaned_words
        
def get_cleaned_words(stopwords):
    """gets the contents of the file and strips the new line 
    param stopwords: contents of the file"""
    for i in stopwords:
        new_stopwords.append(i.strip("\n"))
    return new_stopwords


def get_top_n_words(words,top_n,cleaned_words):
    """gets the individual words and calculates the number of top 5 mostly used words
    param words: individual words of the content,top_n: number of top words,cleaned_words:words free from \n in the file"""
    new_words = []
    for i in words:
        if i not in cleaned_words:
            new_words.append(i)
    top_n_words=Counter(new_words).most_common(top_n)
    top_words=[]
    for x,y in top_n_words:
        top_words.append(x)
    return top_words

