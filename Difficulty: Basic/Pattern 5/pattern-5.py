#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        
        for j in range(N,0,-1):
            for i in range(j):
                print('* ',end = '')
            print() 
        
        
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends