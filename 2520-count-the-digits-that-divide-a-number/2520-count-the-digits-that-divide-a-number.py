class Solution:
    def countDigits(self, num: int) -> int:
        count =0
        n = num
        
        while num >0:
            lastdigit = num %10
            if n % lastdigit ==0:
                count +=1
            num//=10
        return count     
            
        