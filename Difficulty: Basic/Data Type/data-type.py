#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        if str=="Character":
            return 1
        elif str=="Integer":
            return 4
        elif str=="Float":
            return 4
        elif str=="Long":
            return 8
        elif str =="Double":
           return 8
        else:
            return -1
       
#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)
# } Driver Code Ends