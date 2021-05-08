self.num_ways = 0

options = [priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]

self.backtrack(options, dollars, 0)

return self.num_ways


def backtrack (self, options, dollars, i):
    if dollars < 0:
        return

    if i >= len(options):
        self.num_ways += 1
        return

    for product in options[i]:
        self.backtrack(options, dollars - product, i + 1)
