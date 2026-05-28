"""User Configuration Manager Project (freeCodeCamp)

This project supports:
 - Viewing Current Settings
 - Updating System Configurations
 - Deleting Outdated Settings
 - User Choice and Input Validation
"""

def add_setting(Settings, new_setting):
    """Add a new configuration setting to the system.
    Args:
        Settings (dict): The dictionary containing current system settings.
        new_setting (tuple): The key-value pair to be added.
    Returns:
        str: Status message indicating the outcome of the addition attempt.
    """

    # Normalize input to prevent duplicate keys with different casing
    key = new_setting[0].lower()
    value = new_setting[1].lower()

    # Check if the configuration key already exists to prevent duplication
    if key in Settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        Settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(Settings, updated_setting):
    """Update an existing configuration setting in the system.
    Args:
        Settings (dict): The dictionary containing current system settings.
        updated_setting (tuple): The key-value pair to be updated.
    Returns:
        str: Status message indicating the outcome of the update attempt.
    """

    key = updated_setting[0].lower()
    value = updated_setting[1].lower()

    # Verify the setting exists before attempting to modify it.
    if key in Settings:
        Settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(Settings, key):
    """Delete a configuration setting from the system.
    Args:
        Settings (dict): The dictionary containing current system settings.
        key (str): The name of the setting to be deleted.
    Returns:
        str: Status message indicating the outcome of the delete attempt.
    """

    key = key.lower()

    # Verify the setting exists before attempting to delete it
    if key in Settings:
        del Settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(Settings):
    """View the current system configuration settings.
    Args:
        Settings (dict): The dictionary containing current system settings.
    Returns:
        str: System settings in a presentable format.
    """

    # Return a fallback message if the dictionary is empty
    if not Settings:
        return "No settings available."
    else:
        formatted_settings = ''
        # Build a clean, readable string with capitalized keys for presentation
        for key, value in Settings.items():
            formatted_settings += key.capitalize() + ': ' + value + '\n'
        return f"Current System Settings:\n{formatted_settings}"

def view_changes(Settings):
    """Prompt the user to view the updated configuration settings.
    Args:
        Settings (dict): The dictionary containing changed system settings.
    Returns:
        str: The formatted settings if requested, or a confirmation message otherwise.
    """

    answer = input("Would you like to view your settings? (yes/no): ")
    # Standardize input to handle case variations like "Yes" or "YES"
    if answer.lower() == 'yes':
        return view_settings(Settings) + '\n'
    elif answer.lower() == 'no':
        return "Alright!\n"
    else:
        # handles invalid user inputs
        return "I'll take that as a no.\n"

def main():
    print("------------------------------------------")
    print("|              UCS Manager               |")
    print("------------------------------------------")
    print("Configure your settings in just a few steps.")
    print()
    print("Welcome! What would you like to do today?\n")
    print("\t1. Add New Settings")
    print("\t2. Update Current Settings")
    print("\t3. Delete Current Settings")
    print("\t4. View Current Settings\n")

    test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

    ch = input("Select an option: ")
    match ch:
        case '1':
            print(add_setting(test_settings, ('auto-rotate', 'on')),'\n')
            print(view_changes(test_settings))
        case '2':
            print(update_setting(test_settings, ('theme', 'light')),'\n')
            print(view_changes(test_settings))
        case '3':
            print(delete_setting(test_settings, 'volume'),'\n')
            print(view_changes(test_settings))
        case '4':
            print(view_settings(test_settings),'\n')
        case _:
            print("Sorry, I can't help you with that.")

if __name__ == "__main__":
    main()