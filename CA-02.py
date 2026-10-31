tlb_time = 10       
mem_time = 80       

def calculate_eat(h):
    eat = h * (tlb_time + mem_time) + (1 - h) * (tlb_time + 2 * mem_time)
    return eat

h1 = 0.90
print("Case 1")
print("Hit ratio (h):", h1)
print("TLB lookup time:", tlb_time, "ns")
print("Memory access time:", mem_time, "ns")
eat1 = calculate_eat(h1)
print("EAT =", eat1, "ns")

h2 = 0.75
print("\nCase 2")
print("Hit ratio (h):", h2)
print("TLB lookup time:", tlb_time, "ns")
print("Memory access time:", mem_time, "ns")
eat2 = calculate_eat(h2)
print("EAT =", eat2, "ns")

print("\nComparison")
print("EAT at h = 0.90:", eat1, "ns")
print("EAT at h = 0.75:", eat2, "ns")
print("Difference:", eat2 - eat1, "ns")
print("A higher TLB hit ratio gives a lower/better effective access time.")