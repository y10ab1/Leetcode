class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [(h,n) for h,n in zip(heights, names)]
        l.sort()
        return [n for _,n in l][::-1]