"""
Trie class -- will be awesome.
"""


class Trie:

    trie = {}
    indexes = {}
    names = []  # this will store the original pretokenized names

    def __init__(self, copy=None):
        if copy is not None:
            self.trie = copy

    def add_words(self, *words):
        for word in words:
            curr = self.trie
            for letter in word:
                curr = curr.setdefault(letter, {})
            curr = curr.setdefault('_leaf', '_leaf')

    def add_token_words(self, *words):
        for name in words:
            for word in name.split().append(name):
                word = word.lower()
                if word not in self.indexes:
                    self.indexes[word] = [len(self.names)]
                else:
                    self.indexes[word].append(len(self.names))
                curr = self.trie
                for letter in word:
                    curr = curr.setdefault(letter, {})
                curr = curr.setdefault('_leaf', '_leaf')
            self.names.append(name)

    def in_trie(self, word):
        curr = self.trie
        for letter in word:
            if letter in curr:
                curr = curr[letter]
            else:
                return False
        if "_leaf" in curr:
            return True
        else:
            return False

    def remove_words(self, *words):
        for word in words:
            if self.in_trie(word):
                curr = self.trie
                for letter in word:
                    curr = curr[letter]
                curr.pop("_leaf")  # removing leaf node

    def remove_token_words(self, *words):
        for word in words:
            lower_word = word.lower()
            self.remove_words(*lower_word.split())

    def check_token_prefix(self, prefix):
        prefix = prefix.lower()
        retval = []
        curr = self.trie
        for letter in prefix:
            if letter in curr:
                curr = curr[letter]
            else:
                return False  # Fallback on levenshtein
        tokens = map(lambda w: prefix + w, self.all_suffix(curr))
        for token in tokens:
            retval = retval + self.indices_to_names(self.indexes[token])
        return retval

    def indices_to_names(self, indices):
        names = []
        for index in indices:
            names.append(self.names[index])
        return names

    def check_prefix(self, prefix):
        curr = self.trie
        for letter in prefix:
            if letter in curr:
                curr = curr[letter]
            else:
                return False  # Fallback on levenshtein
        return map(lambda w: prefix + w, self.all_suffix(curr))

    def all_suffix(self, curr):
        cum_list = []
        for key in curr.keys():
            if key == "_leaf":
                cum_list = cum_list + [""]
            else:
                cum_list = cum_list + map(lambda w: key + w, self.all_suffix(curr[key]))
        return cum_list


if __name__ == "__main__":
    trie = Trie()
    trie.add_words("dog", "dogma", "dic")
    print trie.in_trie("dog")
    print trie.in_trie("dick")
    print trie.trie
    trie.add_words("fish", "monkey", "money")
    print trie.in_trie("fishy")
    print trie.trie
    trie.remove_words("fish")
    print trie.trie
    print trie.in_trie("fish")
    print trie.check_prefix("dog")
