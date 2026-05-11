from functions.write_file import write_file

def run_tests():
    # Case 1: Overwriting an existing file (lorem.txt)
    print("--- Test 1: Overwrite existing file ---")
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)

    # Case 2: Writing to a new nested directory (pkg/morelorem.txt)
    print("\n--- Test 2: Create directories and write ---")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)

    # Case 3: Attempting to write outside the working directory
    print("\n--- Test 3: Out-of-bounds security check ---")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)

if __name__ == "__main__":
    run_tests()

