sequence = [4, 2, 1, 4, 3, 2, 5, 4]
capacity = 3

cache = [] 
hits = 0
miss = 0

for i in sequence:
    removed = None

    if i in cache:
        hits += 1
        status = "HIT"
        cache.remove(i)
        cache.append(i)
    else:
        miss += 1
        status = "MISS"
        if len(cache) == capacity:
            removed = cache.pop(0)  
        cache.append(i)

    print("Block:", i, "|", status, "| Cache:", cache, "| Removed:", removed)

total = hits + miss
print("\nTotal Hits:", hits)
print("Total Misses:", miss)
print("Hit Ratio:", hits / total)