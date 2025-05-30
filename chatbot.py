import random
import re
import nltk  # Natural Language Toolkit for chatbot functionality
from nltk.chat.util import Chat, reflections  # NLTK's built-in chatbot tools

# Download the NLTK punctuation data (only needed first time)
nltk.download('punkt')

class Chatbot:
    def __init__(self):
        # Store user's name for personalized responses
        self.user_name = None  
        
        # Collection of jokes for when user asks for humor
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
            "How do you organize a space party? You planet!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What do you call a fake noodle? An impasta!",
            "How do you make a tissue dance? Put a little boogie in it!",
            "Why can't you explain puns to kleptomaniacs? They always take things literally!"
        ]
        
        # Conversation patterns and responses
        # Format: [input pattern, possible responses]
        self.pairs = [
            # Greeting patterns
            [r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
            
            # Name identification
            [r'what is your name\??', ["I'm ChatBot 2.0! What's your name?"]],
            
            # User name capture and response
            [r'my name is (.*)', self.get_name_response],
            
            # Help/commands explanation
            [r'what can you do\??|help', ["I can introduce myself, remember your name, tell jokes, and chat! Try asking 'how are you?' or 'tell me a joke'"]],
            
            # Mood/status check
            [r'how are you\??', ["I'm doing great! How about you?", "I'm functioning perfectly today!"]],
            
            # Responding to "how are you?" positively
            [r'(i\'?m|i am|doing)?\s?(good|great|fine|well|okay|awesome)', ["That's great to hear! How can I assist you further?"]],
            
            # Weather-related queries
            [r'(.*) (weather|temperature) (.*)', ["I wish I could check the weather for you! Maybe try a weather app?", "I'm not connected to weather services, but I can tell you a joke instead!"]],
            
            # Joke requests
            [r'(.*) (joke|funny|humor|laugh)', [self.tell_random_joke]],  # Calls the joke-telling method
            
            # Exit commands
            [r'quit|bye|exit', ["Goodbye! Come back soon!", "It was nice talking to you!"]],
            
            # Default catch-all response
            [r'(.*)', ["I'm not sure I understand. Could you ask differently?", "That's interesting! Could you tell me more?"]]
        ]
        
        # Initialize the NLTK chat system with our patterns
        self.chat = Chat(self.pairs, reflections)
    
    def get_name_response(self, match):
        """Store the user's name and return personalized response"""
        self.user_name = match.group(1).capitalize()
        return [f"Nice to meet you, {self.user_name}! How can I help you today?"]
    
    def tell_random_joke(self, match=None):
        """Select and return a random joke from our collection"""
        return random.choice(self.jokes)
    
    def start_chat(self):
        """Main method to start the chatbot interaction"""
        print("\n=== CHATBOT ===")
        print("Type 'quit' to exit\n")
        print("Hello! I'm your friendly chatbot. How can I assist you today?")
        
        while True:
            try:
                # Get user input and clean it up
                user_input = input("You: ").strip()
                
                # Handle empty input
                if not user_input:
                    print("Bot: I didn't catch that. Could you type something?")
                    continue
                    
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    farewell = "Goodbye" + (f", {self.user_name}" if self.user_name else "") + "!"
                    print("Bot:", farewell)
                    break
                
                # Detect positive reaction to jokes
                if re.search(r'\b(fun|funny|awesome|excellent|lol|haha|hilarious)\b', user_input.lower()):
                    print("Bot: I'm glad you liked it! Would you like to hear another joke or need help with something else?")
                    continue

                # Special handling for name introduction
                name_match = re.match(r'my name is (.*)', user_input, re.IGNORECASE)
                if name_match:
                    print("Bot:", self.get_name_response(name_match)[0])
                    continue
                
                # Special handling for joke requests
                if re.search(r'joke|funny|humor|laugh', user_input, re.IGNORECASE):
                    print("Bot:", self.tell_random_joke())
                    continue
                
                # Get response from NLTK chat system
                response = self.chat.respond(user_input)
                
                # Handle different response types
                if isinstance(response, list):
                    print("Bot:", random.choice(response))
                elif response:
                    print("Bot:", response)
                else:
                    print("Bot: I'm not sure what you mean. Maybe try asking differently?")
                    
            # Handle keyboard interrupt (Ctrl+C)
            except KeyboardInterrupt:
                print("\nBot: Goodbye! Thanks for chatting!")
                break
            # Handle other unexpected errors gracefully
            except Exception as e:
                print("Bot: Oops! Something went wrong. Let's try that again.")

# Start the chatbot when script is run directly
if __name__ == "__main__":
    bot = Chatbot()
    bot.start_chat()