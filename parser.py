import numpy as np
import json

#n = np.ndarray([2])
#print(n)

class Domain:

    def load(self, filename):
        f = open(filename, 'r', encoding='utf8')
        self.json = json.load(f)

class KnowledgeGraph:
    def __init__(self):
        a = 0

class QAArray:
    def load(self, filename):
        f = open(filename, 'r', encoding='utf8')
        self.json = json.load(f)

dp = Domain()
dp.load('domain.json')

qa = QAArray()
qa.load("qa.json")

for x in qa.json:
    print(x.keys())
