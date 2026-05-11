from functions.run_python_file import run_python_file

def run_tests():
    print("--- Test 1: main.py (Usage) ---")
    print(run_python_file("calculator", "main.py"))

    print("\n--- Test 2: main.py (Calculation) ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\n--- Test 3: tests.py (Success) ---")
    print(run_python_file("calculator", "tests.py"))

    print("\n--- Test 4: Path Security (Out of bounds) ---")
    print(run_python_file("calculator", "../main.py"))

    print("\n--- Test 5: Non-existent file ---")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\n--- Test 6: Non-python file ---")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    run_tests()

