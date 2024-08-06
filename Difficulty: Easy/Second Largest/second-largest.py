#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        
        
        largest = arr[0]
        s_largest = -1
        
        for i in range(1,len(arr)):
            if arr[i] > largest :
                s_largest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > s_largest :
                s_largest = arr[i]
        
        return s_largest
                
        
        
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends