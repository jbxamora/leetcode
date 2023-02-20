class Solution(object):
    def hasGroupsSizeX(self, deck):
        d = {}
        for x in deck:
            d[x] = d.get(x, 0) + 1
        res = set(d.values())
        if 1 in res: return False
        if len(res) == 1: return True
        div = res.pop()
        for x in res:
            while x:
                div, x = x, div % x
            if div == 1: return False
        return div != 1

