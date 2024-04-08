# def min_elements_to_remove(N, a):
#     # Count occurrences of each element
#     counts = {}
#     for num in a:
#         counts[num] = counts.get(num, 0) + 1

#     # Calculate the number of elements to remove
#     removals = 0
#     for num, count in counts.items():
#         if count > num:
#             removals += count - num

#     return removals

# # Input
n = int(input())
s = list(map(int, input().split()))

numcount = {}
ans=0
for num in s:
    numcount[num]= numcount.get(num,0)+1
for k,val in numcount.items():
    if(k>val):
        ans+=val
    if(k<val):
        ans+= val-k
    
print(ans)
# print(numcount)

