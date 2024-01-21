class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]

        for i in range(1,len(nums)):

            answer.append(answer[i-1]*nums[i-1])
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        
        
            
        return answer
        
            
            