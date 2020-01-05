import discord

import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow
import random
import json
import pickle
import sys
from os import system
import time as t

system("color 0a")
system("title Discord AI Chatbot")

stemmer = LancasterStemmer()

admins = ['Blue Oompa Loompa#8675'] #Admin user account as in the one you would type in to DM someone
clientToken = 'NjYyODA4ODA4MDY1NTk3NDcy.XhEKAA.fsvqQDbJQDPxqecMdW1UTTlAibA'

with open("intents.json") as file:
    global data
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output, tree, unsortedlabels = pickle.load(f)
    global model
    model.load('model.tflearn')
except:
    
    words = []
    labels = []
    docs_x = []
    docs_y = []
    tree = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    unsortedlabels = labels
    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output, tree, unsortedlabels), f)

    tensorflow.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)
    
    model = tflearn.DNN(net)
    try:
        model.load("model.tflearn")
    except:
        model = tflearn.DNN(net) 
        print("training")
        model.fit(training, output, n_epoch=1500, batch_size=8, show_metric=True)
        model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

## Discord ##
client = discord.Client()

userinteract = []

contextTree = ''

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if str(message.author) in admins and message.author in userinteract:
        if message.content == 'exit' or message.content == 'quit' or message.content == 'stop':
            print(str(message.author) + " shut down AI chatbot")
            await message.channel.send(str(message.author) + " shut down AI chatbot")
            await exit()
            
    if message.author in userinteract:
        t.sleep(1)
        results = model.predict([bag_of_words(message.content, words)])[0]
        results_index = np.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            sendToUser = random.choice(responses)
            await message.channel.send(sendToUser)
            print('Sent( "' + str(sendToUser) + '" ) in response to ( "' + message.content + '" ) on the channel ' + str(message.channel))
        else:
            await message.channel.send(str(message.author).split('#')[0] + " sorry I don't understand. :(")
        
        
    if message.content.startswith('$'):
        if message.author in userinteract:
            userinteract.remove(message.author)
        else:
            userinteract.append(message.author)
            await message.channel.send("Hi " + str(message.author) + "!")
            print('Sent( "' + "Hi " + str(message.author) + "!" + '" ) on the channel ' + str(message.channel))
        
client.run(clientToken)
