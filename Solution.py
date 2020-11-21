from collections import defaultdict
lis=input()
n = len(lis)
all_distinct = len(set([a for a in lis]))
substr_count = defaultdict(lambda: 0)
total = 0
start = 0
least_len = n
for j in range(n):
    substr_count[lis[j]] += 1
    if substr_count[lis[j]] == 1:
        total += 1
    if total == all_distinct:
        while substr_count[lis[start]] > 1:
            if substr_count[lis[start]] > 1:
                substr_count[lis[start]] -= 1
            start += 1
        Slice_len = j - start + 1
        if least_len > Slice_len:
            least_len = Slice_len
            pool_start = start
print(len(str(lis[pool_start: pool_start + least_len])))
