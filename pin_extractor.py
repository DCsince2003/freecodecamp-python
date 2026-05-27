"""Pin Extractor Project (freeCodeCamp)

Processes text input and extracts words or PIN-like patterns
using string manipulation techniques.
"""

def pin_extractor(poem):
    """
    Extract secret codes from poems using the length of the nth word
    in the nth line. If missing, use '0'.
    Args:
        poem (str): The poem containing the secret codes
    Returns:
        secret_code (str): The secret code extracted from the poem
    """

    secret_code = ''
    lines = poem.split('\n')

    # Use enumerate() to track line numbers for positional word selection
    for line_index, line in enumerate(lines):
        words = line.split()

        # If the nth word exists in the line, add its length to the secret code; otherwise add '0'.
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
    
    return secret_code

def main():

    poem_1 = """Hold fast to dreams
For if dreams die
Life is a broken-winged bird
That cannot fly."""
    
    poem_2 = """It matters not how strait the gate,
How charged with punishments the scroll,
I am the master of my fate,
I am the captain of my soul."""
    
    poem_3 = """Figure it out for yourself, my lad,
You've all that the greatest of men have had,
Two arms, two hands, two legs, two eyes,
And a brain to use if you would be wise.
With this equipment they all began,
So start for the top and say 'I can.'"""
    
    print("------------------------------------------")
    print("|          Rhyming Xtraction!!!          |")
    print("------------------------------------------")
    print("Are you reading closely? Can you see it?")
    print()
    print(f"A.\n{poem_1}\n\nB.\n{poem_2}\n\nC.\n{poem_3}\n\nD. Custom Poem\n")
    print("Select the serial letter of the poem containing the hidden pin, or choose D to enter your own.")

    ch = input("Enter your choice (A/B/C/D): ")
    if ch in ['A', 'B', 'C', 'D']:

        if ch == 'A':
            pin = pin_extractor(poem_1)

        elif ch == 'B':
            oin = pin_extractor(poem_2)

        elif ch == 'C':
            pin = pin_extractor(poem_3)

        else:
            print("Enter your poem below separated by '\\n' to represent a new line.")
            print("(Note: Do not press Enter until you have finished writing the poem.)")
            poem_text = input()
            poem_4 = '\n'.join(poem_text.split(' \\n '))
            pin = pin_extractor(poem_4)

        print(f"\nHere's your pin - {pin}\n")
    
    else:
        print("\nIt seems you do not have anything for me.\n")

if __name__ == "__main__":
    main()
