from Working1 import Work1

work = Work1()
head = "TIC TAC TOE IN PYTHON"
tail = "THANK YOU FROM PYTHON"
print(head.center(100))
while True:
    print("Your choices :\n1.Enter Game\t2.Exit Game")
    choice = int(input("Enter your choice : "))
    match (choice):
        case 1:
            work.start()
        case 2:
            print(tail.center(100))
            exit()
        case _:
            print("Enter valid choice")
