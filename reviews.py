import pandas as pd
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC


##################################################################################
#                             Read the input data                                #
##################################################################################

train_data = pd.read_csv('train.txt', sep='\t', header=None, names=['title', 'from', 'genre', 'director', 'plot'])

test_data = pd.read_csv('test_no_labels.txt', sep='\t', header=None, names=['title', 'from', 'director', 'plot'])


##################################################################################
#                                Preprocessing                                   #
##################################################################################

stop_words = set(stopwords.words('english')) 
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Remove text in brackets that starts with a capital letter (actors names)
    text = re.sub(r'\(\b([A-Z][a-z]*\s?)+\)', '', text)  
    text = text.lower() 
    text = re.sub(r'http\S+', '', text) 
    text = "".join([i for i in text if i not in string.punctuation])
    words = word_tokenize(text)
    text = " ".join([lemmatizer.lemmatize(i) for i in words if i not in stop_words])
    text = re.sub("\s[\s]+", " ", text).strip()  # Remove repeated/leading/trailing spaces
    return text

train_data['Text_cleaning'] = train_data['plot'].apply(clean_text) 
test_data['Text_cleaning'] = test_data['plot'].apply(clean_text)

##################################################################################
#                                      TF-IDF                                    #                 
##################################################################################

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, max_features=20000)

X_train = tfidf_vectorizer.fit_transform(train_data['Text_cleaning'])
X_test = tfidf_vectorizer.transform(test_data['Text_cleaning'])

##################################################################################
#                                     SVM                                        #                             
##################################################################################

svm = SVC(kernel='linear')
svm.fit(X_train, train_data['genre'])

# Use the trained model to make predictions on the test data
predictions = svm.predict(X_test)

# Save the predictions to 'results.txt' with each predicted genre in a new line
with open('results.txt', 'w') as file:
    for i, genre in enumerate(predictions):
        if i < len(predictions) - 1:
            file.write(genre + '\n')
        else:
            file.write(genre)  # No newline for the last line


print("Predictions saved to results.txt")
