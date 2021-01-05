
arr=(input())
freq=[0]*26
for i in range(len(arr)):
    freq[ord(arr[i])-97]+=1
        
print(freq)
