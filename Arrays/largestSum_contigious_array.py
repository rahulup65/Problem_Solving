subArray_size=int(input())
list_1=list(map(int,input().split()))
sum_of_k=0
for i in range(subArray_size):
    sum_of_k=sum_of_k+list_1[i]
#print(list_1)
#print(sum_of_k)
max_sum_so_far=sum_of_k
window_sum=sum_of_k
l=len(list_1)-subArray_size
for i in range(1,l+1):
    window_sum=window_sum-list_1[i-1]+list_1[i+subArray_size-1]
    if window_sum > max_sum_so_far:
        max_sum_so_far=window_sum
print(max_sum_so_far)        
    













