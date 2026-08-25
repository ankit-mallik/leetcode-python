class Solution:
    def fillCups(self, amount: List[int]) -> int:
        time = 0
        while True:
            amount.sort(reverse=True)
            if amount[0] != 0 and amount[1] != 0:
                amount[0] -= 1
                amount[1] -= 1
                time += 1
            elif amount[0] != 0 and amount[1] == 0:
                amount[0] -= 1
                time += 1
            elif amount[0] == 0:
                return time