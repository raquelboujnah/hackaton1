from sessions import *

def choose_session():
    print("Hello! What type of session would you like to choose?")
    print("1. Yoga")
    print("2. Breathing")
    print("3. Relaxation Meditation")
    print("4. Focus Session")
    print("5. Sleep Aid")
    print("0. Exit")
    

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You chose a Yoga session. Take a deep breath and relax.")
        yoga_session()
    elif choice == "2":
        print("You chose a Breathing session. Breathe in deeply and calmly.")
        breathing_session()
    elif choice == "3":
        print("You chose a Relaxation Meditation session. Close your eyes and let go.")
        meditation_session()
    elif choice == "4":
        print("You chose a Focus session. Focus on your goal and stay calm.")
        focus_session()
    elif choice == "5":
        print("You chose a Sleep Aid session. Breathe slowly and release all tensions.")
        sleep_session()
    elif choice == "0":
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

choose_session()