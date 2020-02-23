
letters = ['f', 'c', 'k', 'r']

words = []
with open('input_text.txt', 'r') as f:
    for line in f:
        line = line.strip()
        words += [*line.split(' ')]

for word in words:
    length = len(word)
    bad_count = 0
    for letter in word:
        if letter in letters:
            bad_count += 1

    res = "good"
    if bad_count > length - bad_count:
        res = "bad"

    print("{} is {}".format(word, res))
