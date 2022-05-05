import pickle

with open('Phrases/Slovak/slovak.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

paragraphs = text.split('\n')

sentences = list()
for paragraph in paragraphs:
    sentences += paragraph.split('. ')

words = list()
for sentence in sentences:
    words += sentence.split(' ')

words_to_del = list()
for i in range(len(words)):
    if len(words[i]) < 3:
        words_to_del.append(words[i])
    elif not words[i][-1].isalpha():
        if not words[i][0].isalpha():
            words_to_del.append(words[i])
        else:
            while not words[i][-1].isalpha():
                words[i] = words[i][:-1]
    elif not words[i][0].isalpha():
        if not words[i][-1].isalpha():
            words_to_del.append(words[i])
        else:
            while not words[i][0].isalpha():
                words[i] = words[i][1:]

words = list(set([word for word in words if word not in words_to_del]))

words_to_del.clear()
for word in words:
    if '.' in word:
        words_to_del.append(word)
words = list(set([word for word in words if word not in words_to_del]))

lengths_amount = dict()
for word in words:
    if len(word) not in lengths_amount:
        lengths_amount[len(word)] = 1
    else:
        lengths_amount[len(word)] += 1

levels_dict = {1: [], 2: [], 3: [], 4: [], 5: [],
               6: [], 7: [], 8: [], 9: [], 10: []}

for word in words:
    if len(word) in (2, 3, 4, ):
        levels_dict[1].append(word)
    elif len(word) in (5, ):
        levels_dict[2].append(word)
    elif len(word) in (6, ):
        levels_dict[3].append(word)
    elif len(word) in (7, ):
        levels_dict[4].append(word)
    elif len(word) in (8, ):
        levels_dict[5].append(word)
    elif len(word) in (9, ):
        levels_dict[6].append(word)
    elif len(word) in (10, 11, ):
        levels_dict[7].append(word)
    else:
        levels_dict[8].append(word)

with open('Phrases/Slovak/phrases.txt', 'r', encoding='UTF-8') as f:
    phrases = f.read()

phrases = phrases.split('\n')

lengths_amount = dict()
for phrase in phrases:
    if len(phrase) not in lengths_amount:
        lengths_amount[len(phrase)] = 1
    else:
        lengths_amount[len(phrase)] += 1

for phrase in phrases:
    if len(phrase) < 15:
        levels_dict[8].append(phrase)
    elif 15 <= len(phrase) < 24:
        levels_dict[9].append(phrase)
    else:
        levels_dict[10].append(phrase)

with open('Phrases/Slovak/dictionary.pickle', 'wb') as f:
    pickle.dump(levels_dict, f)
