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
            ranks.append(new_rank)
            names.append(input("Enter Name: "))
            divs.append(input("Enter Divsion "))
            print("Crew Member added.")
        else:
            print("Invalid Rank. Member not added.")

def remove_member(names, ranks, divs, ids):
    target_id = input("Enter ID to remove: ")
    found_at = -1 
    for i in range(len(ids)):
        if ids[i] == target_id:
            found_at = i 
    if found_at != -1: 
        names.pop(found_at)
        ranks.pop(found_at)
        divs.pop(found_at)
        ids.pop(found_at)
        print("Member removed from system. ")
    else:
        print("ID not found.")

def update_rank(names, ranks, ids):
    target_id = input("Enter ID to update: ")
    for i in range(len(ids)):
        if ids[i] == target_id:
            new_rank = input("Enter new rank for " + names[i] + ": ")
            ranks[i] = new_rank
            print("Rank updated. ")

def search_crew(names, ranks, divs, ids):
    term = input("Enter name to search: ")
    print("\n--- Search Results ---")
    for i in range(len(names)):
        if term in names[i]:
            print("Found:" + names[i] + "| Rank:" + ranks[i] + " | Div:" + divs[i] + " | ID:" + ids[i])

def filter_by_division(names, divs):
    choice = input("Enter Division (Command, Operations, Sciences): ")
    print("--- Members in " + choice + " ---")
    for i in range(len(divs)):
        if divs[i] == choice: 
            print(names[i])

def calculate_payroll(ranks):
    total = 0 
    for r in ranks:
        if r == "Captain":
            total = total + 1000
        elif r == "Commander":
            total = total + 800
        else:
            total = total + 200
    return total 
    
def count_officers(ranks):
    count = 0 
    for r in ranks:
        if r == "Captain" or r == "Commander":
            count = count + 1 
    return count

def main():
    student_name = input("Enter your name to start: ")
    n_list, r_list, d_list, i_list = init_database()
    active = True
    while active == True:
        display_menu(student_name)
        choice = input("Select an option: ")
    
        if choice == "1":
            display_roster(n_list, r_list, d_list, i_list)
        elif choice == "2":
            add_member(n_list, r_list, d_list, i_list)
        elif choice == "3":
            remove_member(n_list, r_list, d_list, i_list)
        elif choice == "4": 
            update_rank(n_list, r_list, i_list)
        elif choice == "5":
            search_crew(n_list, r_list, d_list, i_list)
        elif choice == "6":
            filter_by_division(n_list, d_list)
        elif choice == "7":
            p = calculate_payroll(r_list)
            print("Total Payroll Credits: " + str(p))
        elif choice == "8":
            o = count_officers(r_list)
            print("High Ranking Officers: " + str(o))
        elif choice == "9":
            print("Exiting Fleet Manager. ")
            active = False 
        else: 
            print("Invalid option, try again")
    
main()