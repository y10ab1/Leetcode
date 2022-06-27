class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda course: course[1])
        q = []
        acc_time = 0
        ans = 0
        for dur, end in courses:
            acc_time += dur
            heapq.heappush(q, -dur)
            if acc_time > end:
                acc_time += heapq.heappop(q)
                
            else:
                ans += 1
        return ans
                
        