# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:41:50 2019

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:02:39 2019

@author: User
"""

import nltk
import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
stemming = PorterStemmer()
stops = set(stopwords.words("english"))
try:
    file=open("D:/VITproject/train4.csv","r")
except:
    print("File not found or path is incorrect")
df=pd.read_csv(file,error_bad_lines=False,engine="python")
df.comment=df.comment.astype(str)
def apply_cleaning_function_to_list(X):
    cleaned_X = []
    for element in X:
        cleaned_X.append(clean_text(element))
    return cleaned_X
def clean_text(raw_text):
     # Convert to lower case
    text = raw_text.lower()
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    
    # Keep only words (removes punctuation + numbers)
    # use .isalnum to keep also numbers
    token_words = [w for w in tokens if w.isalpha()]
    
    # Stemming
    #stemmed_words = [stemming.stem(w) for w in token_words]
    # lemmatizing
    lemmatized_words=[lemmatizer.lemmatize(word) for word in token_words]
    
    # Remove stop words
    meaningful_words = [w for w in lemmatized_words if not w in stops]
    # Rejoin meaningful stemmed words
    joined_words = ( " ".join(meaningful_words))
    
    # Return cleaned data
    return joined_words
#test.head(10)
text_to_clean =list(df['comment'])
cleaned_text = apply_cleaning_function_to_list(text_to_clean)
#for i in range(504):
#    #clean=cleaned_text[i]
#    print('Original text:',text_to_clean[i])
#    print ('\nCleaned text:', cleaned_text[i])
#    print('')
#combi=df.append(cleaned_text[i],ignore_index=True)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=CountVectorizer()
vectorizer.fit(cleaned_text)
#print("Vocabulary_content:\n{}".format(vectorizer.vocabulary_))
#print("Features names:"+str(vectorizer.get_feature_names()))
#print(df.shape)
#print(df.info())
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(cleaned_text,df['sentiment'],train_size=0.75,test_size=0.25,random_state=42,shuffle=True) 
#print(X_train.shape,y_train.shape)
Tfidf_vect=TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(cleaned_text)
Train_X_Tfidf=Tfidf_vect.transform(X_train)
Test_X_Tfidf=Tfidf_vect.transform(X_test)
#from sklearn import svm
from sklearn import metrics
#clf=svm.SVC(kernel='linear')
#clf.fit(Train_X_Tfidf,y_train) 
#y_pred=clf.predict(Test_X_Tfidf)
#accuracy=metrics.accuracy_score(y_test,y_pred)*100
#print("Accuracy of the classifier=",round(accuracy,2),'%')
from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()
nb.fit(Train_X_Tfidf,y_train)
#print("Training set score:{:.3f}".format(nb.score(Train_X_Tfidf,y_train)))
#print("Test set score:{:.4f}".format(nb.score(Test_X_Tfidf,y_test)))
pred_nb=nb.predict(Test_X_Tfidf)
confusion=metrics.confusion_matrix(y_test,pred_nb)
#print("Confusion matrix:\n{}".format(confusion))
#text_input=input("Enter the text what you want to type:")
def testing(text_input):
    result=(nb.predict(vectorizer.transform([text_input]))[0])
    if result==1:
        return result
    elif result==0:
        return result
#print(testing("Why was she so upset?"))


    
