import numpy as np
import json
import nltk
import tokenizers as tok


# n = np.ndarray([2])
# print(n)

class Domain:
    def load(self, filename):
        f = open(filename, 'r', encoding='utf8')
        self.json = json.load(f)


class KnowledgeGraph:
    def __init__(self):
        a = 0

    def parse_query(self, q):
        self.currentQ = q


class QAArray:
    def load(self, filename):
        f = open(filename, 'r', encoding='utf8')
        self.json = json.load(f)


dp = Domain()
dp.load('domain.json')

qa = QAArray()
qa.load("qa.json")

kg = KnowledgeGraph()

for x in qa.json:
    for key in iter(x.keys()):
        kg.parse_query(key)
        print(tok.tokzr_WORD(key))
