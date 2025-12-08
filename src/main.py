from scheduler import algo
from sort import slot_key
def main():
    solution = algo()
    sorted_solution = dict(sorted(solution.items(), key=slot_key))
    
    if solution:
        print("\nVALID SCHEDULE FOUND:\n")
        for course, slot in sorted_solution.items():
            print(f"{course:<20} → {slot}")
    else:
        print("\nNo valid schedule exists with the current constraints.\n")


if __name__ == "__main__":
    main()
