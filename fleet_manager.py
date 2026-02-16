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

def display_roster(names, ranks, divs, ids):
    print("\n--- Current Roster ---")
    for i in range (len(names)):
        print("ID: " + ids[i] + " | Name: " + names[i] + " | Rank: " + ranks[i] + " | Div: " + divs[i])

def add_member(names, ranks, divs, ids):
    new_id = input("Enter New ID: ")
    already_exists = False
    for item in ids:
        if item == new_id:
          already_exists = True
    if already_exists == True:
        print("Error: ID already exists")
    else:
        new_rank = input("Enter Rank (Captain, Commander, Ensign):")
        if new_rank == "Captain" or new_rank == "Commander" or new_rank == "Ensign":
            ids.append(new_id)
            ids.append(new_rank)
            names.append(input("Enter Name: "))
            divs.append(input("Enter Divsion "))
            print("Crew Member added.")
        else:
            print("Invalid Rank. Member not added.")
            








