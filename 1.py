#!/usr/bin/python
def fib(n):
    fib_vals = [1, 1, 2]
    for i in xrange(3, n):
        fib_vals.append(fib_vals[i-1] + fib_vals[i-2])
    if n > 1:
        return fib_vals[-1]
    else:
        return n

def main():
    input_value = int(input())
    print fib(input_value)

if __name__ == '__main__':
    main()

