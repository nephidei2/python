#!/usr/bin/python

def counting(string):
    words_freq = dict()
    letters = [str(symbol).lower() for symbol in list(string) if symbol.isalpha()]
    for l in letters:
        if l in words_freq:
            words_freq[l] += 1
        else:
            words_freq[l] = 1
    return words_freq

def main():
    with open('input.txt') as f:
        text = ' '.join(f.readlines())
    freq = counting(text)
    if len(freq) > 0:
        for w in [w[0] for w in sorted(freq.iteritems(), key=lambda(k, v): (-v, k))]:
            print w + ': ' + str(freq[w])
    else:
        print ''

if __name__ == '__main__':
    main()

