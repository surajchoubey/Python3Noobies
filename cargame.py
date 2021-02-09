command = ""
started = False

while True:
    command = input(">").lower()
    if command == "start":
        if not started:
            print("Car started... Ready to go")
            started = True
        else:
            print("Car has already started you bitchy woman karen")
    elif command == "stop":
        if started:
            print("Car stopped... You can pull over")
            started = False
        else:
            print("Stop being a Karen the car has already stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to stop the car
        """)
    elif command == "quit":
        print("Have a nice day sir")
        break
    else:
        print("Sorry,I don't understand this for Christ's Sake")