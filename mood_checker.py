mood = input("Hello there, how are you feeling today? ").casefold()

if mood == "happy":
    print("It's great to see you happy")
elif mood =="nervous":
    print("Take a deep breath 3 times")
elif mood =="sad":
    print("Here's a puppy and a beer. Feel better yet?")
elif mood =="excited":
    print("Yay, adventure!")
elif mood =="relaxed":
    print("Chill")
else:
    print("I don't recognize this mood")
