from flask import Flask
from flask_cors import CORS
import os
import six
from google.cloud import language
from google.cloud.language import enums, types
import pandas as pd
import json
import nltk
from nltk.chat.util import Chat, reflections

credential_path = "credentials.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello,What would you like to eat or drink?", "Hey there,what would you like to cook? Fancy a drink?", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
         "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy", "Ronaldo", "Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ]


]

def analyze_entities(text_content):
    client = language.LanguageServiceClient()
    type_ = enums.Document.Type.PLAIN_TEXT
    lang = "en"
    document = {"content": text_content, "type": type_, "language": lang}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
    response = client.analyze_entities(document, encoding_type=encoding_type)

    return response.entities

def classify_text(text):
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    return categories

def getKeyWords(text):
    #text = "I want an apple pie with lots of cream. I also want to make chicken with mushrooms."
    entities = analyze_entities(text)
    
    results = []
    for entity in entities:
        text = entity.name.rjust(len(entity.name) + 1, " ") * 50
        categories = classify_text(text)
    
        for category in categories:
            if(category.name.startswith("/Food & Drink")) :
                results.append(entity.name)
    
    return results

def getAllRecipies(text): #This doesnt get the reciepes, it gets 5 foods that have that word
    ingredients = []

    search_list = getKeyWords(text) #These are the words identified as food that API would send to this code

    df = pd.read_csv('RAW_recipes.csv', header=0, usecols=['name','ingredients'])
    df['c'] = df.name.str.extract('({0})'.format('|'.join(search_list))) #Looks for the food in the csv

    results = df[~pd.isna(df.c)] #result saves only those rows that contain the words
    results = results.head(5) # limit the results
    results = results.drop(['name'])
    #print(results.name) #name of the dishes
    #print(results.ingredients)
    print(results.values.tolist())
          
    return json.dumps(results.values.tolist())

def chatBot(inp):
    pair = []  
    counter = 0
    
    if inp not in pairs:
      df1 = pd.read_csv('RAW_recipes.csv', header=0, usecols=['name','ingredients', 'steps'])
      df2 = pd.read_csv('mr-boston-flattened.csv', header=0,usecols=['name','instructions','INGREDIENTS'])
      
      df1['name'] = df1['name'].str.lower()
  
      for i in df1['name']:
          j=df1.get_value(counter,2,takeable = True)
          i = r"{}".format(i)
      
          pa=[]
      
          pa.append(i)
          pa.append([j])
          pair.append(pa)
          counter = counter + 1
      
      counter = 0
      for i in df2['name'] :
          j=df2.get_value(counter,2,takeable = True)
          i = r"{}".format(i)
          pa=[]
          pa.append(i)
          pa.append([j])
          pair.append(pa)
          counter = counter + 1



    for i in pairs:
        pair.append(i)

    results=getAllRecipies(inp)
    i = r"{}".format(inp)
    j = r"{}".format(results)
    pa = []
    pa.append(i)
    pa.append([j])
    pair.append(pa)

    i=[
        r"(.*)",
        ["I'm sorry, could you please elaborate or ask for another recipe"]

    ]
    pair.append(pa)

    chat = Chat(pair, reflections)
    return chat.respond(inp)


app = Flask(__name__)
CORS(app)

@app.route('/extract/<text>')
def extract(text):
    #print(*getKeyWords(text))
    print(text)
    return str(getKeyWords(text))

@app.route('/all/<text>')
def all(text):
    return str(getAllIngredients(text))

@app.route('/chat/<inp>')
def converse(inp):
    return chatBot(inp)

if __name__ == '__main__':
    app.run("0.0.0.0", 80, False)

