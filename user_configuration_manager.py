"""User Configuration Manager Project (freeCodeCamp)"""

def add_setting(Settings, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in Settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        Settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(Settings, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in Settings:
        Settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(Settings, key):
    key = key.lower()

    if key in Settings:
        del Settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(Settings):
    if not Settings:
        return "No settings available."
    else:
        formatted_settings = ''
        for key, value in Settings.items():
            formatted_settings += key.capitalize() + ': ' + value + '\n'
        return f"Current User Settings:\n{formatted_settings}"
    
def main():
    test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
    print(add_setting(test_settings, ('auto-rotate', 'on')),'\n')
    print(update_setting(test_settings, ('theme', 'light')),'\n')
    print(delete_setting(test_settings, 'volume'),'\n')
    print(view_settings(test_settings),'\n')
if __name__ == "__main__":
    main()