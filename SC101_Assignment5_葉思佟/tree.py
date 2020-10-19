"""
This file help me to create a trie
I did not create the code by myself, but copy it from someone else's code online
"""


class Trie:
    head = {}
    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True

        else:
            return False
