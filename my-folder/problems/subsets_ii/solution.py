class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        output = [[]]
        for i in nums:
            for j in range(len(output)):
                if not tuple(output[j] + [i]) in seen:
                    output.append(output[j] +[i])
                    seen.add(tuple(output[j]+[i]))
        return output