import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pandas as pd
from pyswip import Prolog

def filtering(sentence):
    others = [',', '.', ';', ':', '@', '#', '/', '|']
    ps = PorterStemmer()
    lem = WordNetLemmatizer()
    filtered_sentence = []
    stemmed_words = []
    lemmatized_words = []
    tokenized_word = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
#     For the removal of special symbols 
    for noise in others:
        stop_words.add(noise)
    for word in tokenized_word:
#         Check if the word is not a stop word
        if word not in stop_words:
            filtered_sentence.append(word)
    for word in filtered_sentence:
        stemmed_words.append(ps.stem(word))
    for word in stemmed_words:
        lemmatized_words.append(lem.lemmatize(word, 'v'))
    return lemmatized_words

def make_rules():
    df_skill = pd.read_csv('skillmap.csv')
    df_skill.head()
    l = df_skill['Skills Element Name'].value_counts()
    l.to_csv('skill.csv')
    k = pd.read_csv('skill.csv')
    data_base = ''
    for i in k['Unnamed: 0']:
        data_base += i + ' '
    l = df_skill['Work Activities Element Name'].value_counts()
    l.to_csv('work.csv')
    k = pd.read_csv('work.csv')
    for i in k['Unnamed: 0']:
        data_base += i + ' '
    others = [',', '.', ';', ':', '@', '#', '/', '|']
    s = set(stopwords.words('english'))
    for noise in others:
        s.add(noise)
    temp = ''
    for i in data_base.split():
        if i not in s:
            temp += i + ' '
    data_base = temp
    data_base = data_base.split(',')
    temp = ''
    for i in data_base:
        temp += i + ' '
    data_base = temp
    print('Career Prediction System by Hrithik Malhotra')
    s = input("Tell me about your interests. I would use this data to improve my prediction system:\n").lower()
    temp = filtering(s)
    standard = 'ai commerce algorithms data electronics science arts open_source finance accounts design academics biology physics chemistry mathematics space statistics history sports economics machine_learning android psychology computers law'
    standard = data_base + standard
    standard_fil = filtering(standard)
    standard = standard.split()
    fact_dict = {}
    index = 0
    for word in standard_fil:
        fact_dict[word] = standard[index]
        index += 1
    rules = list(set(temp) & set(standard_fil))
    return rules, fact_dict
if __name__ == '__main__':
    rules, fact_dict = make_rules()
    with open("prolog.pl", 'a') as f:
        f.write('\n')
        for i in rules:
            f.write('interest(' + fact_dict[i] + ').\n')
    print('Analysis Complete')
    print('Now running Prolog program...')
    code = Prolog()
    code.consult('prolog.pl')
    output = code.query('predict(_).')
    for i in output:
        print(i)