#User function Template for python3
 
class Solution: 
  
    def selectionSort(self, nums,n):
        n = len(nums)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1 , n):
                if nums[j] < nums[min_idx] :
                    min_idx = j

            nums[i] ,nums[min_idx] = nums[min_idx] , nums[i]

        return nums




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends