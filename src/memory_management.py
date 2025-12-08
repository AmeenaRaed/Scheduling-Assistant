from variables import domains
import copy

path_memory = []
domains_memory = []
temp_domains = copy.deepcopy(domains)


def remove_course_from_temp(state):
    course = next(iter(state))
    temp_domains.pop(course, None)
    domains_memory.append(copy.deepcopy(temp_domains))
    

def add_to_path_memory(state):
    if path_memory:
        last_state = path_memory[-1]
        combined = {**last_state, **state}  # merge last + new
    else:
        combined = state
    combined = copy.deepcopy(combined)  # ensure safety
    if combined not in path_memory:
        path_memory.append(combined)

    
def back_to_last_state():
    global temp_domains
    if (len(path_memory)> 1):
        path_memory.pop()
    if (len(domains_memory)> 1):
        domains_memory.pop()
        temp_domains = copy.deepcopy(domains_memory[-1])

def remove_current_value(domains, current):
    course, slot = next(iter(current.items()))

    if course in domains and slot in domains[course]:
        domains[course].remove(slot)