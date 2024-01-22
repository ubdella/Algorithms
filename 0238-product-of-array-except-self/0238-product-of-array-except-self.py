class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        
        for i in range(1, len(nums)):
            answer.append(nums[i-1]*answer[i-1])
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
             
        return answer