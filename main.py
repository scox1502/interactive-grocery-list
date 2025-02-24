# TASK: Create an interactive grocery list manager.
item_list = []
while True:
    # Define a function to add an item to the list
    while True:
        amount_of_items = int(input("how many items do you plan on getting? "))
        if amount_of_items > 0:
            break
      

        elif amount_of_items > 99:
            choice = input(f"damn that's a lot of stuff you sure? [y/n] ").strip().lower()
            if choice == "y":
                break
            else:
                pass
        
        elif amount_of_items == 0:
            print("man put somthing in there now")
            choice = input(f" well are you even getting something? [y/y] ").strip().lower()
            if choice == "y":
                pass

            

    choice = input(f"you want {amount_of_items} idem's? [y/n] ").strip().lower()
    if choice == "y":
        break
    else:
            pass
    
while amount_of_items > 0:
    
    choice = input("Would you like to see your list, add to your list, or delete any idem's? [view/delete/add] ").strip().lower()
    if choice == "view":
        print(f"You have: {item_list}")


    elif choice == "delete":
        delete_item = input(f"type out what item would you like to delete? {item_list} ").strip()
        if delete_item in item_list:
            item_list.remove(delete_item)
            amount_of_items += 1
            print(f"Deleted '{delete_item}' from the list. you have {amount_of_items} item's left.")
        else:
            print(f"'{delete_item}' not found in the list.")



    elif choice == "add":
        item = input(f"What is the {amount_of_items}th item you want to add? ")
        item_list.append(item)  # Add the item to the list
        amount_of_items -= 1
        print(f"Added '{item}'. you have {amount_of_items} items left.")

        
    else:
        print("that is not an option")
        pass
    
if amount_of_items == 0:
    print("you have used up all your slots")
    print(f"Your final list of items: {item_list}")
    choice = input("Would you like to see your list, add to your list, or delete any idem's? [view/delete/add] ").strip().lower()
    
    if choice == "view":
        print(f"You have: {item_list}")
    
    elif choice == "delete":
        delete_item = input(f"type out what item would you like to delete? {item_list} ").strip()
        if delete_item in item_list:
            item_list.remove(delete_item)
            amount_of_items += 1
            print(f"Deleted '{delete_item}' from the list. you have {amount_of_items} item's left.")
            else:
            print(f"'{delete_item}' not found in the list.")



# Append the item to the list and return it


# Define a function to remove an item from the list


# If the item exists, remove it


# If not, display a message saying the item is not in the list


# Define a function to display the grocery list


# If the list is not empty, print all items with numbers


# If the list is empty, display a message


# Start with an empty grocery list


# Use a loop to let the user choose an action:


# (1) Add an item


# (2) Remove an item


# (3) View the list


# (4) Exit the program


# Call the corresponding function based on user input


# Continue looping until the user chooses to exit
