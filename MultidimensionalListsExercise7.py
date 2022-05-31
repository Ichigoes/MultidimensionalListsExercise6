sublist = input().split("|")

result = []

for idx in range(len(sublist) - 1, -1, -1):
    current_result = sublist[idx].strip().split()
    result.extend(current_result)

print(' '.join(result))