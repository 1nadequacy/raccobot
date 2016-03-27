import numpy as np
import re

class DataSet(object):
    def __init__(self, file_name, phrase_len=20, step=2):
        with open(file_name, 'r') as f:
            self.text = f.read().lower()
        self.text = re.sub(r'[^a-z\.,!\?]', ' ', self.text).strip()
        self.text = re.sub(r'\s+', ' ', self.text)
        self.chars = set(self.text)
        self.c2i = {c : i for i, c in enumerate(self.chars)}
        self.i2c = {i : c for i, c in enumerate(self.chars)}
        X, y = [], []
        self.D = len(self.chars)
        self.L = phrase_len
        for i in range(0, len(self.text) - self.L, step):
            xx = np.zeros((self.L, self.D), dtype=np.bool)
            yy = np.zeros(self.D, dtype=np.bool)
            for j in range(self.L):
                xx[j, self.get_id(self.text[i + j])] = True
            yy[self.get_id(self.text[i + phrase_len])] = True
            X.append(xx)
            y.append(yy)
        self.X = np.array(X)
        self.y = np.array(y)

    def get_data(self):
        return self.X, self.y

    def get_char(self, i):
        return self.i2c[i]

    def get_random_phrase(self):
        i = np.random.randint(0, len(self.text) - self.L)
        return self.text[i : i + self.L]

    def get_id(self, c):
        return self.c2i[c]

    def x_to_phrase(self, x):
        assert x.shape[0] == self.L
        assert x.shape[1] == self.D
        return ''.join(self.get_char(np.argmax(i)) for i in x)

    def phrase_to_x(self, phrase):
        assert len(phrase) == self.L
        x = np.zeros((1, self.L, self.D), dtype=np.bool)
        for i in range(self.L):
            x[0, i, self.get_id(phrase[i])] = True
        return x
