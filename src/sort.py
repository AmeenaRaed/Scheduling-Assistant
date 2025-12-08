DAY_ORDER = {
    "Sun": 1,
    "Mon": 2,
    "Tue": 3,
    "Wed": 4,
    "Thu": 5
}
def slot_key(item):
    course, slot = item
    day, time_range = slot.split()
    start = time_range.split("-")[0]  # "11:00"

    hour, minute = map(int, start.split(":"))
    start_minutes = hour * 60 + minute

    return (DAY_ORDER[day], start_minutes)
