import sys
import os

# adding path to find engine file
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ancestry_engine import AncestryEngine

def main():
    print("starting app...")
    # initializing engine
    # make sure rules file is in logic folder
    my_app = AncestryEngine("../logic/family_rules.pl")

    while True:
        print("\n")
        print("    ANCESTRY PROJECT (VITYARTHI)    ")
        print("------------------------------------")
        print("1. Find Relatives")
        print("2. Check Relationship")
        print("3. Full Report")
        print("4. Add Member")
        print("5. Exit")
        print("------------------------------------")
        
        ch = input("Enter choice: ")

        if ch == '1':
            n = input("Enter name: ").lower()
            r = input("Enter relation (sister/brother/father/cousin): ").lower()
            
            print("Finding...")
            ans = my_app.get_relatives(n, r)
            
            if len(ans) > 0:
                print("Result:")
                for x in ans:
                    print("- " + x)
            else:
                print("No result found.")
            
            input("press enter...")

        elif ch == '2':
            p1 = input("Name 1: ").lower()
            r = input("Relation: ").lower()
            p2 = input("Name 2: ").lower()
            
            res = my_app.check_relationship(p1, r, p2)
            
            if res == True:
                print("YES, True.")
            else:
                print("NO, False.")
            
            input("press enter...")

        elif ch == '3':
            n = input("Enter name: ").lower()
            d = my_app.get_family_report(n)
            
            print("\n--- REPORT ---")
            print("Name: " + n)
            print("Parents: ", end="")
            print(d['parents'])
            print("Siblings: ", end="")
            print(d['siblings'])
            print("Ancestors: ", end="")
            print(d['ancestors'])
            
            input("press enter...")

        elif ch == '4':
            name = input("Name: ").lower()
            gen = input("Gender (male/female): ").lower()
            dad = input("Father: ").lower()
            mom = input("Mother: ").lower()
            
            my_app.add_new_member(name, gen, dad, mom)
            print("Added successfully.")
            input("press enter...")

        elif ch == '5':
            print("bye")
            break
        
        else:
            print("wrong input")

if __name__ == "__main__":
    main()
