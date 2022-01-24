#!/usr/bin/env python3

import json
import urllib.request

deck_name = 'words'

with open('words.txt') as f:
    data = f.read()

meanings = data.split('\n\n')
words = []
for entry in meanings:
    lines = entry.split('\n')
    if len(lines) >= 2:
        word = lines[1].split('/')[0]
        words.append(word)

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, word, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        if response['error'] == 'cannot create note because it is a duplicate':
            return 'skip duplicate: ' + word
        raise Exception(response['error'])
    return response['result']

for i in range(len(meanings) - 1):
    # uncomment following two lines and comment last two lines to check
    # what will be added to your deck
    #print("=============={}============".format(words[i][:len(words[i]) - 1]))
    #print(meanings[i+1])
    result = invoke('addNote', words[i], note={'deckName': deck_name, 'modelName': 'Basic', 'fields': {'Front': words[i][:len(words[i]) - 1], 'Back': meanings[i+1]}})
    print(result)
