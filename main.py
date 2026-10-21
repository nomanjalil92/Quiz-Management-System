from quiz import run_quiz
from file_handler import save_result, view_results

def main_menu():
    while True:
        print("\n====== QUIZ MANAGEMENT SYSTEM ======")
        print("1. Start Quiz")
        print("2. View Previous Results")
        print("3. Exit Program")
        print("====================================")
        
        choice = input("Apni choice select karein (1-3): ").strip()

        if choice == '1':
            name, score, total = run_quiz()
            save_result(name, score, total)
            
        elif choice == '2':
            view_results()
            
        elif choice == '3':
            print("\nProgram khatam karne ke liye shukriya. Allah Hafiz!")
            break
            
        else:
            print("\n[ERROR] Ghalat choice! Bara-e-maharbani 1, 2, ya 3 select karein.")

if __name__ == "__main__":
    main_menu()
