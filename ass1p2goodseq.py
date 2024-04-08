def min_elements_to_remove(N, a):
    # Count occurrences of each element
    counts = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1

    # Calculate the number of elements to remove
    removals = 0
    for num, count in counts.items():
        if count > num:
            removals += count - num

    return removals

# Input
N = int(input())
a = list(map(int, input().split()))

# Output
print(min_elements_to_remove(N, a))
