from tool_manager import ToolManager
from medical_information import MedicalInformation

def main():
    manager = ToolManager()

    while True:
        print("\nChoose your selection:")
        print("1. Add")
        print("2. List of all codes")
        print("3. Search")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4):\n")

        if choice == "1":
            item_description = input("Enter item description: ")
            view_search = input("Enter view search: ")
            prob_questions = input("Enter probing questions: ")
            key_word = input("Enter key word: ")

            manager.add_med_info(item_description, view_search, prob_questions, key_word)
            print("All information added successfully!\n")

        elif choice == "2":
            print("\nList of all added descriptions:")
            manager.list_med_info()

        elif choice == "3":
            key_word = input("Enter key word to search: ").strip()

            content = manager.search_med_info(key_word)
            if content:
                print("Medical information found: ")
                print(content)
            else:
                print("Medical information not found!")

        elif choice == "4":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()