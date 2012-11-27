"""
Levenshtein distance module
- Finds the Levenshtein distance between two strings.
- Returns the string in a preset "dictionary" which has the minimum Levenshtein distance between some input word.
Note: we will use memoization to have major performance gains (we will do this with lru_cache)
"""

from functools32 import lru_cache


def lev_distance(a, b):
    """
    Returns the Levenshtein Distance between a and b after the words are lowercased
    """
    return ld(a.lower(), b.lower())


@lru_cache(maxsize=1000)
def ld(a, b):
    """
    Returns the Levenshtein Distance between a and b
    """

    if not a:
        return len(b)  # We must add len_b characters to a, thus this is the LD
    if not b:
        return len(a)  # We must add len_a characters to b, thus this is the LD
    if a[0] == b[0]:
        return lev_distance(a[1:], b[1:])  # In this case, this will be the minimum distance, since it adds no work
    # this takes care of obvious cases, now we just return the min LD of removing the last character from the a, b, or both.
    return min(lev_distance(a, b[1:]), lev_distance(a[1:], b), lev_distance(a[1:], b[1:])) + 1


def nearest_word(a, dictionary):
    """
    Returns the word that is closest to the input word
    dicationary is a list of valid words
    """
    best_choice = dictionary[0]
    best_distance = lev_distance(a, best_choice)
    for word in dictionary[1:]:
        distance = lev_distance(a, word)
        if distance < best_distance:
            best_distance = distance
            best_choice = word
        if distance == 0:
            return best_choice  # no need to continue searching other possibilities
    return best_choice


if __name__ == "__main__":
    # given two command line inputs, returns the distance between the two strings
    import sys
    if len(sys.argv) > 2:
        first = sys.argv[1]
        second = sys.argv[2]
        print "Levenshtein distance between %s and %s is %i" % (first, second, lev_distance(first, second))
    elif len(sys.argv) > 1:
        word = sys.argv[1]
        sample_dict = ['kittens', 'chicken', 'fish', 'dog', 'monkey', 'kangaroo', 'donkey', 'sitting', 'licking', 'muscles', 'communication', 'work', 'hour', 'dancer', 'drink', 'toast', 'university']
        near_word = nearest_word(word, sample_dict)
        print "The closest word to %s in the default dictionary is %s with distance %i" % (word, near_word, lev_distance(word, near_word))
    else:
        print "Levenshtein distance between %s and %s is %i" % ("kittens", "sitting", lev_distance("kittens", "sitting"))
