users = {}

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

# Function to register a user
def register():
    print("\n--- Registration ---")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try logging in.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

# Function to login a user
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found! Please register first.")
        return False
    password = input("Enter your password: ")
    if users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False

# Function to attempt quiz
def attempt_quiz():
    print("\n--- Quiz ---")
    print("Choose a topic: 1. DSA  2. DBMS  3. Python")
    topic_choice = int(input("Enter your choice: "))
    topics = list(questions.keys())
    topic = topics[topic_choice - 1]
    print(f"\nYou selected {topic}.\n")
    
    score = 0
    for q in questions[topic]:
        print(q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        answer = int(input("Your answer (1-4): "))
        if answer == q["answer"]:
            score += 1
    
    print(f"\nYour score in {topic}: {score}/{len(questions[topic])}")
    return score

# Main menu
def main():
    while True:
        print("\n--- Quiz Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            register()
        elif choice == 2:
            if login():
                print("You are now logged in!")
        elif choice == 3:
            attempt_quiz()
        elif choice == 4:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the application
if __name__ == "__main__":
    main()