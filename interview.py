start = '''
You wake up one morning and find that you have your job interview today; you aren't even in your room.
You're in front of the office about to walk in.
A sign is hanging from the window saying the company will open in 5 minutes. Meanwhile you are prepping yourself for your interview.
'''


print(start)


print("Type 'male' if you are male or 'female' if you are female.")
user_input = input()
if user_input == "male":
    print("You will be geting interviewed by a good friend. Do you wish to continue your interview?") # finished the story by writing what happens
    user_input = input()
    if user_input == "yes":
        print("Are you interested in taking this job?")
        user_input = input()
        if user_input == "yes":
            print("Awesome! Congradulations!")
    elif user_input == "no":
        print("Okay, your loss!")

elif user_input == "female":
    if user_input == "yes":
        print("The interviewer walks you to your car and asks")
