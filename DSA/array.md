# sort 0,1,2
```
initialize start=-1,mid=0,end=n-1
iterate from mid to end
if arr[mid]==0 increament start and swap the value of start and mid
elif arr[id]=2 swap value of mid and end and decrement end
else increment mid
```
```
    def sort012(self, arr):
        n=len(arr)
        start=-1
        end=n-1
        i=0
        while i<=end:
            if arr[i]==0:
                start+=1
                arr[start],arr[i]=arr[i],arr[start]
                i+=1
            elif arr[i]==2:
                arr[end],arr[i]=arr[i],arr[end]
                end-=1
            else:
                i+=1
```
# 2 Kadan's algo

```
    def maxSubArraySum(self,arr):
        final=float('-inf')
        res=0
        for i in arr:
            res+=i
            if res>final:
                final=res
            if res<0:
                res=0
        return final
```