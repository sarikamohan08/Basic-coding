def duplicate(arr):
    if(len(arr)==1):
        return arr
    if(arr[0]==arr[1]):
        return duplicate(arr[1:])
    
    return arr[0]+duplicate(arr[1:])
    
def main():
    arr=input()
    #arr=list(st)
    print(duplicate(arr))






































    
main()
