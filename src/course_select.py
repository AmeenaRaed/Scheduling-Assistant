from variables import domains, courses

# Minimum Remaining Values (MRV) heuristic: select the course with the fewest available time slots
def select_course_MRV(assigned):
    unassigned = [c for c in courses if c not in assigned]
    return min(unassigned, key=lambda c: len(domains[c]))
