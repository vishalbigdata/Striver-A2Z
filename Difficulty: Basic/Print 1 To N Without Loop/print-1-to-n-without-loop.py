#User function Template for python3

class Solution:    
    #Complete this function
    
    def printNos(self,N):
        #Your code here
        count = 1
        while(count < N+1):
            print(count,end = ' ')
            count = count + 1
            #Solution.printNos(self,count)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends