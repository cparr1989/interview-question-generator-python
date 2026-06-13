import random

interview_bank = {
    "data analyst": {
        "questions": [
            "Tell me about a time you used data to solve a problem.",
            "How do you clean messy data?",
            "Explain the difference between SQL and Excel.",
            "How would you explain a dashboard to a non-technical manager?",
            "What would you do if your data showed unexpected results?"
        ],
        "keywords": ["data", "analysis", "excel", "sql", "dashboard", "report", "clean", "insight"]
    },
    "healthcare": {
        "questions": [
            "How do you protect patient confidentiality?",
            "Tell me about a time you handled sensitive information.",
            "How do you stay organized in a fast-paced healthcare setting?",
            "What would you do if you found an error in a patient record?",
            "How do you handle stressful situations?"
        ],
        "keywords": ["hipaa", "patient", "confidentiality", "records", "accuracy", "compliance", "care"]
    },
    "banking": {
        "questions": [
            "How would you handle a transaction discrepancy?",
            "Tell me about a time you gave excellent customer service.",
            "How do you stay accurate when handling money?",
            "What would you do if a customer became upset?",
            "How do you prevent errors?"
        ],
        "keywords": ["accuracy", "customer", "service", "cash", "transaction", "policy", "detail"]
    }
}

def choose_category():
    print("Mock Interview Coach")
    print("--------------------")
    print("1. Data Analyst")
    print("2. Healthcare")
    print("3. Banking")

    choice = input("Choose a career field: ")

    if choice == "1":
        return "data analyst"
    elif choice == "2":
        return "healthcare"
    elif choice == "3":
        return "banking"
    else:
        print("Invalid choice. Defaulting to Data Analyst.")
        return "data analyst"

def score_answer(answer, keywords):
    answer = answer.lower()
    score = 0
    matched_keywords = []

    for keyword in keywords:
        if keyword in answer:
            score += 1
            matched_keywords.append(keyword)

    return score, matched_keywords

def give_feedback(score, matched_keywords):
    print("\nFeedback Report")
    print("---------------")

    print("Matched Keywords:", ", ".join(matched_keywords) if matched_keywords else "None")

    if score >= 5:
        print("Rating: Strong Answer")
        print("Your answer includes strong role-related language.")
    elif score >= 3:
        print("Rating: Good Answer")
        print("Your answer is solid, but could use more specific examples.")
    elif score >= 1:
        print("Rating: Needs Improvement")
        print("Try adding more job-related keywords and a real example.")
    else:
        print("Rating: Weak Answer")
        print("Try using the STAR method: Situation, Task, Action, Result.")

def run_mock_interview():
    category = choose_category()
    questions = random.sample(interview_bank[category]["questions"], 3)
    keywords = interview_bank[category]["keywords"]

    total_score = 0

    print(f"\nStarting {category.title()} Mock Interview")
    print("Answer each question like you are in a real interview.")

    for question in questions:
        print("\nQuestion:")
        print(question)

        answer = input("Your answer: ")

        score, matched_keywords = score_answer(answer, keywords)
        total_score += score

        give_feedback(score, matched_keywords)

    print("\nFinal Interview Report")
    print("----------------------")
    print(f"Total Score: {total_score}")

    if total_score >= 12:
        print("Overall Result: Excellent interview performance.")
    elif total_score >= 7:
        print("Overall Result: Good performance. Add stronger examples.")
    else:
        print("Overall Result: Needs practice. Use STAR answers and include more role-specific details.")

run_mock_interview()
