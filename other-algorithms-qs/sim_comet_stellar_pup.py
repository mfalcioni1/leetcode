import random
def roll():
    return random.randint(1,6)

def activate(damage: int, counter: int, activations: int):
    if roll() <= 2:
        return damage + 2, counter + 2, activations + 1
    elif roll() <= 3:
        return damage, counter - 1, activations + 1
    elif roll() <=5:
        return damage + counter, counter - 2, activations + 1
    else:
        damage, counter, activations = activate(damage, counter + 1, activations + 1)
        return activate(damage, counter + 1, activations + 1)

def main(iters):
    results = {"damage": [], "counter": [], "activations": []}
    for _ in range(iters):
        d, c, a = activate(0, 5, 0)
        results["damage"].append(d)
        results["counter"].append(c)
        results["activations"].append(a)
    return results

n = 1000000
r = main(n)
sum([i >= 20 for i in r["damage"]])/(n/100)
