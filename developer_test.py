from collections import Counter


def checkout(products):
    market = {
        'CH1': 3.11,
        'AP1': 6.00,
        'CF1': 11.23,
        'MK1': 4.75,
        'OM1': 3.69
    }

    count_by_item = Counter(products)

    total = 0

    for k, v in Counter(products).items():

        if k == 'CH1':
            total += market[k] * v
            continue

        # Buy-One-Get-One-Free Special on Coffee.
        if k == 'CF1':
            total += (v - (v//2)) * market[k]
            continue

        # If you buy 3 or more bags of Apples, the price drops to $4.50.
        if k == 'AP1':
            total += (market[k] * v) - (v // 3 * 4.50)
            continue

        # Purchase a bag of Oatmeal and get 50% off a bag of Apples
        if k == 'OM1':
            total += (market[k] * v) - (count_by_item['AP1'] * market['AP1'] / 2)

        # Purchase a box of Chai and get milk free. (Limit 1)
        if k == 'MK1' and 'CH1' in products:
            total += market[k] * (v - 1)
            continue
        else:
            total += market[k] * v
            continue

    return total

if __name__ == '__main__':
    assert checkout(['CH1', 'AP1', 'CF1', 'MK1']) == 20.34
    assert checkout(['MK1', 'AP1']) == 10.75
    assert checkout(['CF1', 'CF1']) == 11.23
    assert checkout(['AP1', 'AP1', 'CH1', 'AP1']) == 16.61
