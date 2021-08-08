class Node:
    def __init__(self):
        self.next = {}
        self.depth = 0
        self.words = set()
        self.last = False

class WordTrie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.insert(word)

    def insert(self, word):
        n = self.root
        for w in word:
            if w not in n.next:
                n.next[w] = Node()
                n.next[w].depth = n.depth + 1
            n.words.add(word[n.depth:])
            n = n.next[w]
        n.last = True

class AutoComplete(WordTrie):
    def __init__(self, words):
        super().__init__(words)

    def suggest(self, keyword):
        n = self.root
        for k in keyword:
            if k not in n.next: return []
            n = n.next[k]
        a = []
        if n.last: a.append(keyword)
        for word in n.words:
            a.append(keyword + word)
        return a


a = AutoComplete(['한글', 'gone', 'guild', 'word', 'war', 'warrior', 'world'])
print(a.suggest('하'))      # ['go', 'gone']
print(a.suggest('한'))      # ['guild']
print(a.suggest('w'))       # ['warrior', 'world', 'word', 'war']
print(a.suggest('wa'))      # ['war', 'warrior']
print(a.suggest(''))        # ['guild', 'warrior', 'go', 'war', 'world', 'gone', 'word']
print(a.suggest('gc'))