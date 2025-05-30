# AI-Chatbot-With-NLP
A friendly Python chatbot that tells jokes, remembers your name, and responds to your reactions with natural conversation.

**COMPANY:** CODETECH IT SOLUTIONS

**Name:** Anjali Dilip Patel

**INTERN ID:** CT06DL927

**Domain:** Python Programming

**BATCH Duration:** 6 Weeks

**Mentor:** Neela Santhosh Kumar

**PROJECT:** AI CHATBOT WITH NLP 

## Overview

This chatbot is an interactive terminal-based application that showcases foundational **Natural Language Processing (NLP)** techniques using Python's **NLTK** library. The bot demonstrates how regex-based pattern recognition can create engaging and semi-personalized conversations.

## Key Features

- *Pattern-based NLP*: Uses regular expressions to understand user inputs
- *Personalization*: Remembers and uses the user's name
- *Humor Integration*: Includes a collection of jokes for interactive fun
- *Graceful Conversation Handling*: Manages user inputs, errors, and exits smoothly
- *Fallback Responses*: Provides meaningful replies when inputs are unrecognized

## Technical Implementation

- Developed in **Python 3.x**
- Leverages **NLTK's Chat module** and `reflections`
- Implements custom logic for name capturing and joke delivery
- Uses `re` (regex) for dynamic user input handling
- Contains robust error and exit handling for smooth user experience

## Requirements

- Python 3.6 or higher
- NLTK library
  
  ```bash
  pip install nltk
  ```

## Installation & Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/AI-Chatbot-With-NLP.git
   cd AI-Chatbot-With-NLP
   ```

2. **Install Dependencies:**

   ```bash
   pip install nltk
   ```

3. **Download NLTK Data (Only First Time):**

   ```python
   import nltk
   nltk.download('punkt')
   ```

4. **Run the Chatbot:**

   ```bash
   python chatbot.py
   ```

## How It Works

* Captures user input and matches it with predefined regex patterns.
* Applies basic reflection and template responses for interaction.
* Uses custom Python logic for specific input types (e.g., name or joke request).
* Includes fallback for unmatched inputs and exit handling.

## Example Interactions

![image](https://github.com/user-attachments/assets/7787e71d-4b51-4104-a504-d2791e9b65ac)

## Academic Relevance

This project helps demonstrate:

* Regex-based text pattern matching
* NLP chatbot fundamentals
* Dialogue state tracking (e.g., remembering user name)
* Practical application of the NLTK library

## License

* **This project**: [MIT License](LICENSE) - Free to use, modify, and distribute
