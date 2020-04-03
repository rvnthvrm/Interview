def substring(inp):
    result = [inp[i: j] for i in range(len(inp)) for j in range(i + 1, len(inp) + 1)]
    final_out = []
    for i in result:
        if len(i) == len(set(i)):
            final_out.append(i)

    o = list(set(final_out))
    print('All Substrings: ', o)
    print('Largest Substring: ', max(o, key=len))


if __name__ == '__main__':
    inp = "aabbbabcdeefghi"
    substring(inp)
