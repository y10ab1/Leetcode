class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_numbers = {2:['a','b','c'],
                         3:['d','e','f'],
                         4:['g','h','i'],
                         5:['j','k','l'],
                         6:['m','n','o'],
                         7:['p','q','r','s'],
                         8:['t','u','v'],
                         9:['w','x','y','z']}
        ans = []
        for d in digits:
            temp_ans = []
            for s in phone_numbers[int(d)]:
                temp = []
                if ans:
                    for a in ans:
                        temp.append(a+s)
                else:
                    temp.append(s)
                temp_ans += temp
            ans = temp_ans
        return ans
