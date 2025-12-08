from constraints import valid_assignment
from variables import domains
from memory_management import path_memory, domains_memory, temp_domains, remove_current_value
from algo_helpers import preprocess_domains, generate_root, generate_next_state

def algo ():
    global domains
    originalSize = len(domains)
    domains = preprocess_domains()  # Sort once!
    domains_memory.append(temp_domains)
    while domains:
        current = generate_root() ## Pick most promising domain
        if current is None: ## No more branches to check --> No solution
            break
        
        next_state = generate_next_state(current) ## Try to generate next valid state (this function may get back to previous state if it found no valid state)
        while(next_state is not None): ## When it's none, this means we either have reach to deadend for the root or found a valid solution
            next_state = generate_next_state(next_state)
        
        ## Check if solution is found
        if (len(path_memory) == 0 or not valid_assignment(path_memory[-1]) or len(path_memory[-1]) != originalSize): ## if it's invalid, it means we are in deadend, we need to pick other root
            remove_current_value(domains, current) ## we remove the root from the original list of domains
        else:
            return path_memory[-1] ## valid solution found
    return None ## no valid solution found
    
    
        
# def algo(assigned={}):
#     if len(assigned) == len(courses):
#         if valid_assignment(assigned):
#             return assigned
#         return None

#     course = [c for c in courses if c not in assigned][0]

#     for slot in domains[course]:
#         new_assignment = assigned.copy()
#         new_assignment[course] = slot

#         if valid_assignment(new_assignment):
#             result = algo(new_assignment)
#             if result:
#                 return result

#     return None