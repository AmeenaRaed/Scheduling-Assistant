from scheduler import algo
def main():
    solution = algo()

    if solution:
        print("\nVALID SCHEDULE FOUND:\n")
        for course, slot in solution.items():
            print(f"{course:<20} → {slot}")
    else:
        print("\nNo valid schedule exists with the current constraints.\n")


if __name__ == "__main__":
    main()
