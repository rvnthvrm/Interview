def efficient_janitor(weight):
    weight.sort()
    l = 0
    r = len(weight) - 1
    c = 0
    while l <= r:
        if l == r:
            break
        if weight[l] + weight[r] <= 3.0:
            l += 1
            r -= 1
            c += 1
        else:
            r -= 1
            c += 1

    return c


if __name__ == '__main__':
    a = [4, 1.01, 1.991, 1.32, 1.4]
    print(efficient_janitor(a))
