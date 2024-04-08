n = input()
mylist = list(map(int,input().split()))
ans_list = []
flag = True
for num in mylist:
    if(num%2 != 0):
        flag=False
        break
    else :
        cnt =0
        tmp = num
        while True:
            tmp=tmp/2
            cnt+=1
            if(tmp%2 != 0):
                ans_list.append(cnt)
                break

if flag:
    print(min(ans_list))
else:
    print(0)
