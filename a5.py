
words = []
with open('input_text.txt', 'r') as f:
    for line in f:
        line = line.strip()
        words += [*line.split(' ')]

for word in words:
    if (len(word) > 3):
        first_letter = word[0]
        print("{}{}ay".format(word[1:], first_letter))
    else:
        print(word)