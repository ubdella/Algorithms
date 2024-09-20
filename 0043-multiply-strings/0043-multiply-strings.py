class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize the result array with zeros
        res = [0] * (len(num1) + len(num2)) 
        
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) -1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos, nextPos = i + j + 1, i + j
                total = mul + res[pos]
                res[pos] = total % 10
                res[nextPos] += total // 10
        res = map(str, res)
        return "".join(res).lstrip("0")
