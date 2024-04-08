word = input()
ans = 0
L_count = 0
R_count = 0
ans_list = set()

st = ""

for ch in word:
    st+=ch
    if ch == 'L':
        L_count+=1
    elif ch == 'R':
        R_count+=1
    # if(L_count>0 and R_count>0 and L_count!= R_count and ch == 'L'):
    #     L_count=0
    #     R_count=0
    #     continue
    if L_count == R_count :
        ans+=1
        ans_list.add(st)
        st=""
        L_count=0
        R_count=0

print(len(ans_list))

for val in ans_list:
    print(val)

# for i in range(0,ans):
#     print(ans_list[i]*'L'+ans_list[i]*'R')