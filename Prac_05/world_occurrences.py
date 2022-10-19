"""
Word Occurrences
Estimate: 40 minutes
Actual:   57 minutes
"""

# words = "this is a collection of words of nice words this is a fun thing it is".split() #  test
words = input("Write some words: ").split()
word_to_count = {}
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 0
    word_to_count[word] += 1
max_length = max(len(word) for word in word_to_count.keys())
for word, number in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {number:2}")
