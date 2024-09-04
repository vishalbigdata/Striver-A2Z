#User function Template for python3

class Solution:
    
    
    '''
    
    arr1 = [1,1,2,3,4,5]
    
    
    arr2 = [2,3,4,4,5,6]
    
    
    '''
    
    
    
    
    
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        
        i, j = 0, 0  # Pointers
        union = []  # Union list
        
        while i < len(arr1) and j < len(arr2) :
            
            # compare value of each array bw them
            
            if arr1[i] <= arr2[j]:
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i = i+1
            else:
                if len(union) == 0 or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j = j+1
        
        while i < len (arr1):
            if union[-1] != arr1[i]:
                union.append(arr1[i])
            i = i + 1
            
        while j < len (arr2):
            if union[-1] != arr2[j]:
                union.append(arr2[j])
            j = j + 1
        
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