class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        l1 = s1.split(" ")
        l2 = s2.split(" ")
        res = []
        
        
        d = dict()
        for i in l1:
            if i in d.keys():
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for i in l2:
            if i in d.keys():
                d[i] = d[i] + 1
            else:
                d[i] = 1
                
        for k,v in d.items():
            if v == 1:
                res.append(k)

        return res
            




    
       


        