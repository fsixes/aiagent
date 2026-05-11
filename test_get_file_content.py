from functions.get_file_content import get_file_content

def run_tests():
    # Case 1: Lorem Ipsum (Truncation test)
    print("--- Testing Truncation (lorem.txt) ---")
    lorem_result = get_file_content("calculator", "lorem.txt")
    print(f"Content Length: {len(lorem_result)}")
    print(f"Truncation message present: {'truncated' in lorem_result}")
    
    # Case 2: Standard file
    print("\n--- Testing main.py ---")
    print(get_file_content("calculator", "main.py"))

    # Case 3: Nested file
    print("\n--- Testing pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # Case 4: Outside working directory
    print("\n--- Testing /bin/cat (Security Check) ---")
    print(get_file_content("calculator", "/bin/cat"))

    # Case 5: Non-existent file
    print("\n--- Testing Non-existent file ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


run_tests()
