filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("Error: Permission denied. You don't have access to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
