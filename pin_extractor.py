def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

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

    print(pin_extractor([poem_1, poem_2, poem_3]))

if __name__ == "__main__":
    main()