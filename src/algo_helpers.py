import random
from constraints import valid_assignment, time_overlap
from variables import domains
from memory_management import path_memory, temp_domains, remove_course_from_temp, add_to_path_memory, back_to_last_state

def count_conflicts(course, slot, domains):
    conflicts = 0

    for other_course, other_slots in domains.items():
        if other_course == course:
            continue

        for other_slot in other_slots:
            if time_overlap(slot, other_slot):
                conflicts += 1

    return conflicts

def preprocess_domains():
    ## Sort domains dictionary by conflict count
    sorted_pairs = []
    
    for course, slots in domains.items():
        for slot in slots:
            conflicts = count_conflicts(course, slot, domains)
            sorted_pairs.append((conflicts, course, slot))
    
    # Sort by conflicts (ascending)
    sorted_pairs.sort(key=lambda x: x[0])
    
    # Rebuild as dictionary with sorted order
    sorted_domains = {}
    for conflicts, course, slot in sorted_pairs:
        if course not in sorted_domains:
            sorted_domains[course] = []
        sorted_domains[course].append(slot)
    
    return sorted_domains

#Heuristic function that picks most promising domain according to number of conflicts
def generate_root():
    ## Pick the first available course-slot pair (already sorted by conflicts)
    for course, slots in domains.items():
        if slots:  # Check if course has available slots
            return {course: slots[0]}  # Return first slot
    return None  # No courses left


def generate_next_state(current_state):
    #Remove domain of the same course as current_state course (key)
    remove_course_from_temp(current_state)
    # Pick next domain randomly from temp_domains
    next_domain = pick_next_domain(current_state)
    if next_domain is None: # We reached a deadend or solution
        return None
    
    add_to_path_memory(next_domain)
    next_state = path_memory[-1]
    if (not valid_assignment(next_state)):
        back_to_last_state()
        if path_memory:
            return path_memory[-1] 
        else:
            return None
    return next_state

def pick_next_domain(current):
    if not temp_domains:
        return None
    course = random.choice(list(temp_domains.keys()))
    timing = random.choice(temp_domains[course])
    return {course: timing}
