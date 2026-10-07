import random

# ============================================
# DAILY LIFE RULE-BASED CHATBOT
# ============================================

print("=" * 50)
print("           🤖 MY DAILY LIFE CHATBOT")
print("=" * 50)
print("Hi! I'm your friendly chatbot.")
print("Let's have a simple conversation about daily life.")
print("You can type 'bye' anytime to exit.")
print("=" * 50)


# ============================================
# FUNCTION TO CHECK EXIT
# ============================================

def is_exit(message):
    return message.lower().strip() in [
        "bye", "exit", "quit", "goodbye"
    ]


# ============================================
# GET USER NAME
# ============================================

while True:
    name = input("\nBot: What's your name?\nYou: ").strip()

    if is_exit(name):
        print("Bot: Goodbye! 👋")
        exit()

    if name:
        break

    print("Bot: Please tell me your name. 😊")


print(f"\nBot: Nice to meet you, {name.capitalize()}! 😊")


# ============================================
# GREETING
# ============================================

greetings = [
    f"Nice to talk with you, {name.capitalize()}! 😊",
    f"Hope you're having a great day, {name.capitalize()}! 🌟",
    f"It's lovely chatting with you, {name.capitalize()}! 👋"
]

print("Bot:", random.choice(greetings))


# ============================================
# MAIN CONVERSATION
# ============================================

while True:

    # ----------------------------------------
    # HOW WAS YOUR DAY?
    # ----------------------------------------

    day = input(
        "\nBot: How was your day today?\nYou: "
    ).strip()

    if is_exit(day):
        break

    if not day:
        print("Bot: That's okay! 😊")
    elif any(word in day.lower() for word in
             ["good", "great", "nice", "awesome", "happy", "excellent"]):
        print("Bot: That's wonderful to hear! 😄")
    elif any(word in day.lower() for word in
             ["bad", "sad", "boring", "tired", "stress", "difficult"]):
        print("Bot: I'm sorry to hear that. ❤️")
        print("Bot: I hope things get better soon!")
    else:
        print("Bot: Thanks for sharing that with me! 😊")


    # ----------------------------------------
    # DAILY ACTIVITY
    # ----------------------------------------

    activity = input(
        "\nBot: What did you do today?\nYou: "
    ).strip()

    if is_exit(activity):
        break

    if not activity:
        print("Bot: You can tell me anything you did today. 😊")
    elif "college" in activity.lower():
        print("Bot: Nice! 📚 How was college today?")
    elif "school" in activity.lower():
        print("Bot: That's nice! 🏫 How was school today?")
    elif "work" in activity.lower() or "office" in activity.lower():
        print("Bot: Sounds like you had a busy day! 💼")
    elif "home" in activity.lower():
        print("Bot: Staying at home can be relaxing! 🏠")
    else:
        print("Bot: Sounds interesting! 👍")


    # ----------------------------------------
    # ENJOYMENT
    # ----------------------------------------

    enjoy = input(
        "\nBot: Did you enjoy your day?\nYou: "
    ).strip().lower()

    if is_exit(enjoy):
        break

    if enjoy in ["yes", "yeah", "yep", "sure", "of course"]:
        print("Bot: That's great! I'm happy for you. 😊")
    elif enjoy in ["no", "nope", "not really"]:
        print("Bot: That's okay. Tomorrow can be a better day! 🌟")
    else:
        print("Bot: I understand! 😊")


    # ----------------------------------------
    # MORNING ROUTINE
    # ----------------------------------------

    morning = input(
        "\nBot: What do you usually do in the morning?\nYou: "
    ).strip()

    if is_exit(morning):
        break

    if "exercise" in morning or "gym" in morning:
        print("Bot: That's a healthy way to start the day! 💪")
    elif "breakfast" in morning:
        print("Bot: Breakfast is important! 🍳")
    elif "college" in morning or "school" in morning:
        print("Bot: Sounds like a productive morning! 📚")
    else:
        print("Bot: Nice morning routine! ☀️")


    # ----------------------------------------
    # FAVORITE FOOD
    # ----------------------------------------

    food = input(
        "\nBot: What is your favorite food?\nYou: "
    ).strip()

    if is_exit(food):
        break

    if food:
        print(
            f"Bot: Wow! {food.capitalize()} sounds delicious! 🍴"
        )
    else:
        print("Bot: You don't have a favorite food? 😄")


    # ----------------------------------------
    # FAVORITE DRINK
    # ----------------------------------------

    drink = input(
        "\nBot: What is your favorite drink?\nYou: "
    ).strip()

    if is_exit(drink):
        break

    if drink:
        print(
            f"Bot: Nice! {drink.capitalize()} sounds refreshing! 🥤"
        )


    # ----------------------------------------
    # FAVORITE COLOR
    # ----------------------------------------

    color = input(
        "\nBot: What is your favorite color?\nYou: "
    ).strip()

    if is_exit(color):
        break

    if color:
        print(
            f"Bot: {color.capitalize()} is a beautiful choice! 🎨"
        )


    # ----------------------------------------
    # FREE TIME / HOBBY
    # ----------------------------------------

    hobby = input(
        "\nBot: What do you like to do in your free time?\nYou: "
    ).strip()

    if is_exit(hobby):
        break

    hobby_lower = hobby.lower()

    if "music" in hobby_lower or "song" in hobby_lower:
        print("Bot: That's nice! Music is a great way to relax. 🎵")
    elif "game" in hobby_lower or "gaming" in hobby_lower:
        print("Bot: Sounds fun! 🎮")
    elif "movie" in hobby_lower or "film" in hobby_lower:
        print("Bot: Watching movies is a great way to relax! 🎬")
    elif "read" in hobby_lower or "book" in hobby_lower:
        print("Bot: Reading is a wonderful hobby! 📚")
    elif "cricket" in hobby_lower or "football" in hobby_lower:
        print("Bot: That's awesome! Sports are always fun! 🏏")
    else:
        print("Bot: That's a great hobby! 😊")


    # ----------------------------------------
    # MUSIC
    # ----------------------------------------

    music = input(
        "\nBot: What kind of music do you like?\nYou: "
    ).strip()

    if is_exit(music):
        break

    if music:
        print(
            f"Bot: Nice! {music.capitalize()} music sounds interesting! 🎵"
        )


    # ----------------------------------------
    # FAVORITE MOVIE
    # ----------------------------------------

    movie = input(
        "\nBot: What is your favorite movie?\nYou: "
    ).strip()

    if is_exit(movie):
        break

    if movie:
        print(
            f"Bot: Nice choice! 🎬 "
            f"{movie.capitalize()} sounds interesting."
        )


    # ----------------------------------------
    # STUDY / WORK
    # ----------------------------------------

    study = input(
        "\nBot: Are you studying, working, or doing something else?\nYou: "
    ).strip()

    if is_exit(study):
        break

    study_lower = study.lower()

    if "student" in study_lower or "study" in study_lower:
        print("Bot: That's great! Keep working hard. 📚")
    elif "work" in study_lower or "job" in study_lower:
        print("Bot: That's great! I hope you're enjoying your work. 💼")
    else:
        print("Bot: Sounds good! Keep doing what you enjoy. 😊")


    # ----------------------------------------
    # TRAVEL
    # ----------------------------------------

    travel = input(
        "\nBot: Do you like traveling? (yes/no)\nYou: "
    ).strip().lower()

    if is_exit(travel):
        break

    if travel in ["yes", "yeah", "yep", "sure", "of course"]:
        print("Bot: That's wonderful! Traveling is exciting! 🌍")

        place = input(
            "\nBot: Where would you like to travel?\nYou: "
        ).strip()

        if is_exit(place):
            break

        if place:
            print(
                f"Bot: {place.capitalize()} sounds like "
                "a beautiful place to visit! 🏔️"
            )
        else:
            print("Bot: I hope you get to visit a beautiful place someday! 😊")

    elif travel in ["no", "nope", "not really"]:
        print("Bot: That's perfectly fine! 😊")
        print("Bot: Maybe you prefer relaxing at home.")

    else:
        print("Bot: I wasn't sure about your answer, but traveling can be fun! 🌍")


    # ----------------------------------------
    # WEEKEND
    # ----------------------------------------

    weekend = input(
        "\nBot: What do you usually do on weekends?\nYou: "
    ).strip()

    if is_exit(weekend):
        break

    weekend_lower = weekend.lower()

    if "sleep" in weekend_lower or "rest" in weekend_lower:
        print("Bot: Sounds relaxing! 😴 Everyone needs some rest.")
    elif "friend" in weekend_lower:
        print("Bot: Spending time with friends is always fun! 👥")
    elif "family" in weekend_lower:
        print("Bot: Family time is special! ❤️")
    elif "movie" in weekend_lower:
        print("Bot: A movie weekend sounds great! 🎬")
    else:
        print("Bot: That sounds like a nice weekend! 😊")


    # ----------------------------------------
    # EVENING
    # ----------------------------------------

    evening = input(
        "\nBot: What do you usually do in the evening?\nYou: "
    ).strip()

    if is_exit(evening):
        break

    if "walk" in evening.lower():
        print("Bot: Evening walks can be very relaxing! 🌆")
    elif "study" in evening.lower():
        print("Bot: That's productive! 📚")
    elif "game" in evening.lower():
        print("Bot: Sounds fun! 🎮")
    elif "music" in evening.lower():
        print("Bot: Music is a great way to relax in the evening! 🎵")
    else:
        print("Bot: Sounds like a nice evening routine! 😊")


    # ----------------------------------------
    # SLEEP
    # ----------------------------------------

    sleep = input(
        "\nBot: What time do you usually go to sleep?\nYou: "
    ).strip()

    if is_exit(sleep):
        break

    if sleep:
        print("Bot: Getting enough sleep is important. 😴")


    # ----------------------------------------
    # FINAL QUESTION
    # ----------------------------------------

    continue_chat = input(
        "\nBot: Would you like to continue chatting? (yes/no)\nYou: "
    ).strip().lower()

    if continue_chat in [
        "no", "nope", "bye", "exit", "quit", "goodbye"
    ]:
        break

    elif continue_chat in [
        "yes", "yeah", "yep", "sure", "of course"
    ]:
        print("\nBot: Great! Let's continue our conversation! 😄")

    else:
        print("\nBot: I'll take that as a yes! Let's continue! 😊")


# ============================================
# END OF CHAT
# ============================================

print("\n" + "=" * 50)
print(f"Bot: It was really nice talking with you, {name.capitalize()}! 😊")
print("Bot: Have a wonderful day! Take care! 👋")
print("=" * 50)
print("              CHAT ENDED")
print("=" * 50)