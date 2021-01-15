class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:
        dict1={}
        for i in range(0,len(releaseTimes)):
            if i==0:
                dict1[keysPressed[i]]=abs(0-releaseTimes[i])
            else:
                if keysPressed[i] in dict1:
                    val=dict1[keysPressed[i]]
                    dict1[keysPressed[i]]=max(abs(releaseTimes[i-1]-releaseTimes[i]),val) 
                else:
                    dict1[keysPressed[i]]=abs(releaseTimes[i-1]-releaseTimes[i])
        val=max(list(dict1.values()))
        dict3=dict(sorted(dict1.items(), key=lambda item: item[0],reverse=True))
        a=list(dict3.keys())[list(dict3.values()).index(val)]
        return str(a) 
s=Solution()
arr=[23,34,43,59,62,80,83,92,97]
st="qgkzzihfc"
print(s.slowestKey(arr,st))        