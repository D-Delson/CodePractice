freq = {}
line = input()

for word in line.split():
    freq[word] = freq.get(word, 0) + 1

sort_freq = sorted(freq.items())

for w, count in sort_freq:
    print('%s %d' % (w, count))