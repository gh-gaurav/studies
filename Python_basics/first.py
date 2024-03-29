from collections import Counter
l1 = ['red','red','blue','black','green','black','green','blue','red']
cnt = Counter()
for c in l1:
    cnt[c]+=1
print(cnt)
