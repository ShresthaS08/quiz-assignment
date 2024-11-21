import json
import os

# File paths for user data and scores
USER_DATA_FILE = "users.json"
SCORES_FILE = "scores.json"

# Initialize data
def load_data(file_path, default_value):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return default_value

users = load_data(USER_DATA_FILE, {})
user_scores = load_data(SCORES_FILE, {})

# Quiz questions
questions = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", 
         "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], 
         "answer": 2},
        {"question": "Which data structure is used for BFS traversal?", 
         "options": ["Stack", "Queue", "Array", "Linked List"], 
         "answer": 2}
    ],
    "DBMS": [
        {"question": "Which SQL keyword is used to fetch data?", 
         "options": ["UPDATE", "FETCH", "SELECT", "WHERE"], 
         "answer": 3},
        {"question": "What is a primary key?", 
         "options": ["A unique identifier for a table row", "A foreign key", "An index", "None of these"], 
         "answer": 1}
    ],
    "Python": [
        {"question": "Which keyword is used to define a function in Python?", 
         "options": ["func", "define", "def", "lambda"], 
         "answer": 3},
        {"question": "What is the output of len([1, 2, 3])?", 
         "options": ["1", "2", "3", "4"], 
         "answer": 3}
    ]
}

# Save data to file
def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# Function to register a user
def register():
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try logging in.")
        return
    password = input("Enter a password: ")
    users[username] = password
    user_scores[username] = {}
    save_data(USER_DATA_FILE, users)
    save_data(SCORES_FILE, user_scores)
    print("Registration successful!")

# Function to login a user
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found! Please register first.")
        return None
    password = input("Enter your password: ")
    if users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Incorrect password!")
        return None

# Function to attempt quiz
def attempt_quiz(username):
    print("\n--- Quiz ---")
    print("Choose a topic: 1. DSA  2. DBMS  3. Python")
    topic_choice = input("Enter your choice: ")
    if topic_choice not in ["1", "2", "3"]:
        print("Invalid choice! Returning to main menu.")
        return
    
    topics = list(questions.keys())
    topic = topics[int(topic_choice) - 1]
    print(f"\nYou selected {topic}.\n")
    
    score = 0
    for q in questions[topic]:
        print(q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        answer = input("Your answer (1-4): ")
        if not answer.isdigit() or int(answer) not in range(1, 5):
            print("Invalid input! Skipping this question.")
            continue
        if int(answer) == q["answer"]:
            score += 1
    
    print(f"\nYour score in {topic}: {score}/{len(questions[topic])}")
    user_scores[username][topic] = score
    save_data(SCORES_FILE, user_scores)

# Main menu
def main():
    logged_in_user = None
    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. View Scores")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            logged_in_user = login()
        elif choice == "3":
            if logged_in_user:
                attempt_quiz(logged_in_user)
            else:
                print("You need to log in first!")
        elif choice == "4":
            if logged_in_user:
                print("\n--- Your Scores ---")
                if logged_in_user in user_scores:
                    for topic, score in user_scores[logged_in_user].items():
                        print(f"{topic}: {score}/{len(questions[topic])}")
                else:
                    print("No scores available!")
            else:
                print("You need to log in first!")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the application
if __name__ == "__main__":
    main()