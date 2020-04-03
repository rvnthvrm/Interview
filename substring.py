def substring(inp):
    result = [inp[i: j] for i in range(len(inp)) for j in range(i + 1, len(inp) + 1)]
    final_out = [i for i in result if len(i) == len(set(i))]
    o = list(set(final_out))
    print('All Substrings: ', sorted(o))
    print('Largest Substring: ', max(o, key=len))


if __name__ == '__main__':
    inp = "aabbbabcdeefghi"
    substring(inp)

    
```
########### OUTPUT #######################
In [3]: inp = "aabbbabcdeefghi"
   ...: substring(inp)
All Substrings:  ['a', 'ab', 'abc', 'abcd', 'abcde', 'b', 'ba', 'bc', 'bcd', 'bcde', 'c', 'cd', 'cde', 'd', 'de', 'e', 'ef', 'efg', 'efgh', 'efghi', 'f', 'fg', 'fgh', 'fghi', 'g', 'gh', 'ghi', 'h', 'hi', 'i']
Largest Substring:  abcde
```
    
