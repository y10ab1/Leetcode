class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(nums,low,high):
            if low>high:return -1
            mid = (low+high)//2
            print(nums[mid], target)
            if target == nums[mid]: return mid
            elif target > nums[mid]: return BS(nums,mid+1,high)
            elif target < nums[mid]: return BS(nums,low,mid-1)
        return BS(nums,0,len(nums)-1)