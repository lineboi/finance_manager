import sys
transactions = []
def menu():
    menu=["Add income","Add expense","view summary","View all transactions ", "Exit"]
    print ("Welcome to the personal finance tracker \n Please select an option:")
    while True:
        for  i,item in enumerate(menu):
            print (f"{i+1} . {item}")

        try:
            choice= int (input("enter your choice (1-5) :"))
            if 1<=choice<=len(menu):
               print(f"You want to : {menu[choice-1]}")
               if choice==5:
                   print ("good bye")
                   sys.exit()
               
            else:
               print(f"Invalid choice . please try again (1-{len(menu)})")
        except ValueError:
            print("wrong input")
        



menu()



