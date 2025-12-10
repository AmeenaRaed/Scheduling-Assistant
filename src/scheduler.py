from constraints import valid_assignment
from variables import domains, courses
from course_select import select_course_MRV
        
def algo(assigned={}):
    if len(assigned) == len(courses):
        if valid_assignment(assigned):
            return assigned
        return None

    course = select_course_MRV(assigned)

    for slot in domains[course]:
        new_assignment = assigned.copy()
        new_assignment[course] = slot

        if valid_assignment(new_assignment):
            result = algo(new_assignment)
            if result:
                return result

    return None