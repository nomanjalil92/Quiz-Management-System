FILENAME = "results.txt"
def save_result(name, score, total_questions):
    """student ka nam or score file main save karta ha."""
    try:
        with open(FILENAME, "a") as file:
            file.write(f"Name:{name} | Score : [score]/{total_questions}\n")
        print("\n[SUCCESS] Aapka result safely save kar diya gaya hai!")
    except IOError:
        print("\n[ERROR] File mein data save karte waqt koi masla pesh aaya.")

def view_results():
    """File se purane results read karke display karta hai."""
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("\nAbhi tak koi purana result maujood nahi hai.")
            return

        print("\n=== Previous Quiz Results ===")
        for line in lines:
            print(line.strip())
        print("=============================")
        
    except FileNotFoundError:
        print("\n[ERROR] 'results.txt' file nahi mili! Abhi tak koi quiz nahi khela gaya.")
    except IOError:
        print("\n[ERROR] File read karte waqt koi masla pesh aaya.")
