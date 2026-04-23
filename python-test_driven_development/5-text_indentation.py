def text_indentation(text):
    """
    Prints text with 2 new lines after ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # This flag tracks if we are at the start of a new line
    # to help us skip leading spaces.
    skip_space = True

    for char in text:
        if skip_space and char == " ":
            continue
        
        # Once we hit a non-space character, stop skipping
        skip_space = False
        
        print(char, end="")

        # If we hit a special character, print newlines and 
        # set flag to skip the next spaces
        if char in ".?:":
            print("\n")
            skip_space = True
