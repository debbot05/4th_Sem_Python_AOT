def read_questions(file_path):
    with open(file_path, 'r') as file:
        questions = [line.strip() for line in file.readlines()]
    return questions

def read_answers(file_path):
    with open(file_path, 'r') as file:
        answers = [line.strip() for line in file.readlines()]
    return answers

def display_quiz(questions, answers):
    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")
        options = ["A", "B", "C", "D"]  # You can customize the options as needed
        for option in options:
            print(f"{option}. {input(f'Enter option {option}: ')}")

    print("\nCorrect Answers:")
    for i, answer in enumerate(answers, start=1):
        print(f"Question {i}: {answer}")

if __name__ == "__main__":
    questions_file_path = "Questions.txt"  # Replace with the actual path to your Questions.txt file
    answers_file_path = "Answers.txt"      # Replace with the actual path to your Answers.txt file

    questions = read_questions(questions_file_path)
    answers = read_answers(answers_file_path)

    display_quiz(questions, answers)
