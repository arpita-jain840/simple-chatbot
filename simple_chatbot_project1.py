import random
import datetime

greetings = ["hello", "hi there", "namaste", "bonjour", "kya haal chaal", "Hello"]
farewells = ["bye", "goodbye", "see you later", "bye bye"]
quotations = ["Try in such a way that while losing,you never know when you win",
              "Be patient, life will give you everything you deserve.",
              "Learn to appreciate what you have,because many people crave for it.",
              "To set an example,you have to make your own path."]
emojis = ["😄", "🎉", "😊", "🤩", "🥰"]


responses = {
    "hi" : "Hello!",
    "bye" : "Goodbye!",
    "how are you?" : "I am fine😊",
    "what is your name?" : "I am a Chatbot🤖",
    "who created you?": "I was created by a beginner programmer 😎",
}


print("CHATBOT IS RUNNING (TYPE Bye TO IT.....) ")
print("YOU CAN \n 1)GREET \n 2)ASK QUOTATIONS \n 3)DATE AND TIME \n 4)EMOJIS \n 5)CALCULATE \n 6)FAREWELL(BYE)")


while True:
    user = input("You: ").lower()


    if user in["bye", "exit", "quit", "stop", "Bye", "Quit"]:
        print("Bot:", random.choice(farewells))
        print("Bot: Thank You!, Hope you enjoy this chatbot🥰")
        break


    elif any(word in user for word in ["hi", "hello", "hey", "hii", "hola"]):
        print("Bot:", random.choice(greetings))


    elif "quotations" in user or "motivational_quote" in user:
        print("Bot:", random.choice(quotations))


    elif "date and time" in user:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")   
        current_date = now.strftime("%d-%m-%Y")   
        print(f"Bot: Today is {current_date} and current time is {current_time}")


    elif "day" in user:
        today = datetime.datetime.now().strftime("%A")
        print("Bot: Today is", today)



    elif "funny" in user or "happy" in user or "awesome" in user:
        print("Bot:", random.choice(emojis))   


    elif "calculate" in user:
        try:
            expr = user.replace("calculate", "").strip()
            result = eval(expr)
            print("Bot: The answer is", result)
        except:
            print("Bot: Sorry, I can't calculate that 😅")
        
    elif user in responses:
        print("Bot:", responses[user])

    else:
        print("Bot: ", responses.get(user, "Sorry! I don't understand"))

