# okay, here's my attempt at a chatbot. probably dumb but whatevs ¯\_(ツ)_/¯
# might add stuff later... or not. who knows?

def chatty_bot():
    print("Heyyy! I'm ChattyBot (not the smartest tho). Type 'bye' when you wanna peace out.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "":
            print("Chatty: Uh... you there? You gotta say *something* lol.")
            continue

        if user_input in ['hi', 'hello', 'hey', 'yo']:
            print("Chatty: Yo! Wassup?")
        elif "how are you" in user_input or "how r u" in user_input:
            print("Chatty: Eh, surviving. You good?")
        elif "your name" in user_input or "who are you" in user_input:
            print("Chatty: Call me ChattyBot. Or just Chatty. Or... whatever you want, really.")
        elif "help" in user_input:
            print("Chatty: Honestly, not much I can do yet. Just chat with me? That's it for now.")
        elif "joke" in user_input:
            print("Chatty: Why did the programmer quit his job? Because he didn't get arrays. Ha. Ha. Ha. ...Okay, I'll stop.")
        elif user_input in ['bye', 'exit', 'quit', 'peace']:
            print("Chatty: Aight, catch you later. Don't be a stranger!")
            break
        else:
            print("Chatty: Hmm... I got nothing for that. Try saying something else?")

        # forgot to add more stuff here... oops lol

if __name__ == "__main__":
    chatty_bot()
