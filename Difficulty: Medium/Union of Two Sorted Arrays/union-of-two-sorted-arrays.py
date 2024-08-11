#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        i, j = 0, 0  # Pointers
        union = []  # Union list
    
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:  # Case 1 and 2
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:  # Case 3
                if len(union) == 0 or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
    
        while i < len(arr1):  # If any elements left in arr1
            if union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
    
        while j < len(arr2):  # If any elements left in arr2
            if union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    
        return union
                
           
            
       
  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends