import json
import string
import random 
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer 
import tensorflow as tf 
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense, Dropout
nltk.download("punkt")
nltk.download("wordnet")

data = {"intents": [
    {"tag": "greeting",
     "patterns": ["Hello", "How are you?", "Hi there", "Hi", "Whats up"],
     "responses": ["Howdy Partner!", "Hello", "How are you doing?", "Greetings!", "How do you do?"],
    },
    {"tag": "age",
     "patterns": ["how old are you?", "when is your birthday?", "when was you born?"],
     "responses": ["I am 21 years old", "I was born in 1999", "My birthday is October 31st and I was born in 1999", "31/10/1999"]
    },
    {"tag": "date",
     "patterns": ["what are you doing this weekend?",
"do you want to hang out some time?", "what are your plans for this week"],
     "responses": ["I am available all week", "I don't have any plans", "I am not busy"]
    },
    {"tag": "name",
     "patterns": ["what's your name?", "what are you called?", "who are you?"],
     "responses": ["My name is Zofo", "I'm Zofo", "Zofo"]
    },
    {"tag": "goodbye",
     "patterns": [ "bye", "g2g", "see ya", "adios", "cya", "tata"],
     "responses": ["It was nice speaking to you", "See you later", "Speak soon!"]
    }
]}

#Initializing lemmatizer to get stem of words
lemmatizer = WordNetLemmatizer()

#Each list to create
words=[]
classes=[]
doc_x=[]
doc_y=[]

#Loop through all intents, tokenize each pattern and append tokens to words, the patterns and the associated tag to their associated list
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        doc_x.append(pattern)
        doc_y.append(intent["tag"])

    #Add the tag to the classes if it's not there already
    if intent["tag"] not in classes:
        classes.append(intent["tag"])
    
#Lemmatize all words in the vocab and convert it to lowercase if the words don't appear in punctuation
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]

#Sorting the vocab and the classes in alphabetical order and taking set so no duplicates occur
words = sorted(set(words))
classes = sorted(set(classes))

#print("Words : \n", words)
#print("\n\n Classes : \n", classes)
#print("\n\n Doc_x : \n", doc_x)
#print("\n\n Doc_y : \n", doc_y)

#List for training data
training = []
out_empty = [0] * len(classes)

#Creating bag or words model
for idx, doc in enumerate(doc_x):
    bow = []
    text = lemmatizer.lemmatize(doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)

    #Mark the index of the class that the current pattern is associated to
    out_row = list(out_empty)
    out_row[classes.index(doc_y[idx])] = 1

    #Add the one hot encoded BoW and the associated classes to training
    training.append([bow, out_row])

#Shuffle the data and convert it to a NumPy array
random.shuffle(training)
training = np.array(training, dtype=object)

#Split the feature and the target labels
train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# NEURAL NETWORK TRAINING:

# defining some parameters
input_shape = (len(train_x[0]),)
output_shape = len(train_y[0])
epochs = 200
# the deep learning model
model = Sequential()
model.add(Dense(128, input_shape=input_shape, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(output_shape, activation = "softmax"))
adam = tf.keras.optimizers.Adam(learning_rate=0.01, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=["accuracy"])
print(model.summary())
model.fit(x=train_x, y=train_y, epochs=200, verbose=1)

# UTILITIES

def clean_text(text): 
  tokens = nltk.word_tokenize(text)
  tokens = [lemmatizer.lemmatize(word) for word in tokens]
  return tokens

def bag_of_words(text, vocab): 
  tokens = clean_text(text)
  bow = [0] * len(vocab)
  for w in tokens: 
    for idx, word in enumerate(vocab):
      if word == w: 
        bow[idx] = 1
  return np.array(bow)

def pred_class(text, vocab, labels): 
  bow = bag_of_words(text, vocab)
  result = model.predict(np.array([bow]))[0]
  thresh = 0.2
  y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]

  y_pred.sort(key=lambda x: x[1], reverse=True)
  return_list = []
  for r in y_pred:
    return_list.append(labels[r[0]])
  return return_list

def get_response(intents_list, intents_json): 
  tag = intents_list[0]
  list_of_intents = intents_json["intents"]
  for i in list_of_intents: 
    if i["tag"] == tag:
      result = random.choice(i["responses"])
      break
  return result

  # running the chatbot
while True:
    message = input("Enter : ")
    intents = pred_class(message, words, classes)
    result = get_response(intents, data)
    print(result)