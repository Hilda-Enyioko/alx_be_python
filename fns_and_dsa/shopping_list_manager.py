# Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(new_item)

        elif choice == '2':
            # Prompt for and remove an item
            removed_item = input("Enter the item you want to remove: ").strip().lower()
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)

            elif removed_item not in shopping_list:
                print (f"{removed_item} is not an item on your shopping list: {shopping_list}")

        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
            
        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()