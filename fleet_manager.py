def init_database():
    names = ["Jean-Luc Picard", "William Riker", "Data", "Geordi La Forge", "Deanna Troi"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lt. Commander", "Commander"]
    divs = ["Command", "Command", "Operations", "Operations", "Sciences"]
    ids = ["1", "2", "3", "4", "5"]
    return names, ranks, divs, ids

def display_menu(student_name):
    print("\n--- STAR FLEET MANAGER ---")
    print("Logged in as student: " + student_name)
    print("1. View Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    
