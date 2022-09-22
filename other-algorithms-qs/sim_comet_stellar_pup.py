import random
def roll():
    return random.randint(1,6)

def activate(life: int, counter: int, blockers: int):
    r = roll()
    if counter <= 0:
        return life, counter, blockers
    if r <= 2:
        return life, counter + 2, blockers - 2
    elif r <= 3:
        return life, counter - 1, blockers
    elif r <=5:
        return life - counter, counter - 2, blockers
    else:
        life, counter, blockers = activate(life, counter + 1, blockers)
        return activate(life, counter, blockers)

def main(iters: int, life: int, blockers: int):
    results = {"life": [], "counter": [], "blockers": [], "win": []}
    for _ in range(iters):
        l, c, b = activate(life, 5, blockers)
        results["counter"].append(c)
        results["blockers"].append(b)
        if blockers < 0:
            life+=blockers
        if life <= 0:
            results["win"].append("yes")
        else:
            results["win"].append("no")
        results["life"].append(l)
    return results

n = 100000
r = main(n, 20, 0)
sum([i <= 0 for i in r["life"]])/(n/100)