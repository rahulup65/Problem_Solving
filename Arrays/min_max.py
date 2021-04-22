def Find_max_min(arr):
    maxi=arr[0]
    mini=arr[0]
    for i in range(len(arr)):
        if mini >arr[i]:
            mini=arr[i]


        if maxi < arr[i]:
            maxi=arr[i]

    print(mini)
    print(maxi)            







n=list(map(int,input().split()))
Find_max_min(n)