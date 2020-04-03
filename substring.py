def substring(inp):
    result = [inp[i: j] for i in range(len(inp)) for j in range(i + 1, len(inp) + 1)]
    final_out = []
    for i in result:
        if len(i) == len(set(i)):
            final_out.append(i)

    print(list(set(final_out)))


if __name__ == '__main__':
    inp = "aabbbabcdeefghi"
    substring(inp)
