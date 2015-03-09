#!/usr/bin/python
def cut_sent(sent, val):
    if len(sent) > int(val):
        spaces = [i for (i, sl) in enumerate(list(sent)) if (sl == ' ' and i <= int(val))]
        if len(spaces) > 0:
            cut = spaces[-1]
            print sent[:cut]
            if len(sent[cut+1:]) < int(val):
                print sent[cut+1:]
            else:
                cut_sent(sent[cut+1:], val)
        else:
            for piece in sent.split(' '):
                print piece
    else:
        print sent

def cut(text, val):
    for sent in text:
        cut_sent(sent, val)

def main():
    with open('input.txt') as f:
        text = f.readlines()
    freq = cut([piece.rstrip() for piece in text[1:]], text[0])

if __name__ == '__main__':
    main()

