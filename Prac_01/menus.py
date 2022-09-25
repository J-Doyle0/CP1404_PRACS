"""
CP1404 - Practical 1
Menus
"""


name = input("Enter name: ")
menu = input("(H)ello\n(G)oodbye\n(Q)uit\n").upper()
while menu != "Q":
    if menu == "H":
        print(f"Hello {name}")
    elif menu == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    menu = input("(H)ello\n(G)oodbye\n(Q)uit\n").upper()
print("Finished.")
