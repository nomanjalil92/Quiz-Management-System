# quiz.py
QUESTIONS = [
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["A. Zardari", "B. Noman Jalil", "C. Quaid-e-Azam", "D. Imran khan"],
        "answer": "C"
    },
    {
        "question": "Python file ki extension kya hoti hai?",
        "options": ["A. .py", "B. .python", "C. .pt", "D. .pyt"],
        "answer": "A"
    },
    {
        "question": "What is the color of Sky?",
        "options": ["A. Red", "B. Blue", "C. Violet", "D. yellow"],
        "answer": "B"
    },
    {
        "question": "Python mein list banane ke liye kaun si brackets use hoti hain?",
        "options": ["A. {}", "B. ()", "C. <>", "D. []"],
        "answer": "D"
    },
    {
        "question": "Python mein single line comment ke liye kya use hota hai?",
        "options": ["A. //", "B. #", "C. /*", "D. <!--"],
        "answer": "B"
    }
]

def calculate_score(correct_answers):
    return correct_answers

def run_quiz():
    print("\n--- Welcome to the Quiz ---")
    
    # Khali naam ko reject karne ke liye loop
    while True:
        name = input("Apna naam darj karein: ").strip()
        if name:
            break
        print("[ERROR] Naam khali nahi choda ja sakta. Dobara koshish karein.")

    score = 0
    total = len(QUESTIONS)

    # Questions display karne ke liye loop
    for index, q in enumerate(QUESTIONS, 1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q['options']:
            print(option)
            
        # Invalid option handle karne ka loop
        while True:
            user_ans = input("Aapka jawab (A, B, C, D): ").strip().upper()
            if user_ans in ['A', 'B', 'C', 'D']:
                break
            print("[ERROR] Ghalat choice! Sirf A, B, C, ya D select karein.")
            continue

        if user_ans == q['answer']:
            score += 1

    total_score = calculate_score(score)
    print(f"\n=== Quiz Complete, {name}! ===")
    print(f"Aapka Total Score hai: {total_score}/{total}")
    
    return name, total_score, total
