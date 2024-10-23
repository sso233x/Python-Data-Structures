def read_file_list(filename):
    file = open(filename, 'r')  # Open the file in read mode
    lines = file.readlines()  # Read all lines from the file
    file.close()  
    
    # Loop through lines and print each with a "-" in front
    for line in lines:
        line = line.strip()  
        print(f"- {line}")
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
read_file_list("dogs")
    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!