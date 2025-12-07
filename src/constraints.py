# format: Mon 8:00-9:15

different_day_pairs = [
    ("AI", "Cloud Computing"),
    ("Web Development", "UI/UX Design")
]

# cannot_take_together_pairs = [
#     # ("Data Science", "Mobile Development"),
#     ("Algorithms", "DevOps")
# ]

same_day_pairs = [
    ("AI", "Algorithms"),
    ("Cloud Computing", "Operating Systems")
]

max_courses_per_day_limit = {
    "Mon": 2,
    "Tue": 2,
    "Wed": 2,
    "Thu": 2,
    "Sun": 2
}

# 1: No time overlap
def time_overlap(slot1, slot2):
    day1, time1 = slot1.split()
    day2, time2 = slot2.split()
    if day1 != day2:
        return False
    start1, end1 = [int(t.replace(":", "")) for t in time1.split('-')]
    start2, end2 = [int(t.replace(":", "")) for t in time2.split('-')]
    return max(start1, start2) < min(end1, end2)

def no_time_conflict(course1, course2, assigned):
    return not time_overlap(assigned[course1], assigned[course2])

# 2: Specific pairs must be on different days
def different_day(course1, course2, assigned):
    if (course1, course2) in different_day_pairs or (course2, course1) in different_day_pairs:
        return assigned[course1].split()[0] != assigned[course2].split()[0]
    return True

# # 4: Can't take specific courses together
# def cannot_take_together(course1, course2, assigned):
#     if (course1, course2) in cannot_take_together_pairs or (course2, course1) in cannot_take_together_pairs:
#         return False
#     return True


# 5: Must be same day
def same_day(course1, course2, assigned):
    if (course1, course2) in same_day_pairs or (course2, course1) in same_day_pairs:
        return assigned[course1].split()[0] == assigned[course2].split()[0]
    return True

# 6: Max courses per day
def max_courses_per_day(assigned):
    day_counts = {}
    for slot in assigned.values():
        day = slot.split()[0]
        day_counts[day] = day_counts.get(day, 0) + 1
    
    for day, limit in max_courses_per_day_limit.items():
        if day_counts.get(day, 0) > limit:
            return False
    return True


def valid_assignment(assigned):
    courses = list(assigned.keys())

    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            c1, c2 = courses[i], courses[j]

            if not no_time_conflict(c1, c2, assigned):
                return False
            if not different_day(c1, c2, assigned):
                return False
            # if not cannot_take_together(c1, c2, assigned):
            #     return False
            if not same_day(c1, c2, assigned):
                return False

    if not max_courses_per_day(assigned):
        return False

    return True