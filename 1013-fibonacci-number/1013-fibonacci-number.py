class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        while True :
            return Solution.fib(self,n-1) + Solution.fib(self,n-2)
       
