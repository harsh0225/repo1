class ChatBot:
    def _init_(self):
        self.responses = {
            "hi": "Hey! What can I help you with?",
            "hello": "Hello! How can I assist you?",
            "how are you?": "I'm doing well, thank you!",
            "what's your name?": "I'm a chatbot. You can call me Chat.",
            "ask me something": "Sure, what would you like to know?",
            "bye": "Goodbye! Have a great day!",
            "thank you": "You're welcome!",
            "default": "I'm sorry, I don't understand that question."
        }

    def get_response(self, query):
        query_lower = query.lower()
        if query_lower in self.responses:
            return self.responses[query_lower]
        else:
            return self.responses["default"]

# Create a new instance of the ChatBot
my_bot = ChatBot()

# Test the responses
while True:
    user_input = input("You: ").strip().lower()
    if user_input == 'quit':
        print("ChatBot: Goodbye!")
        break
    response = my_bot.get_response(user_input)
    print("ChatBot:", response)