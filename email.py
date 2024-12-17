email = input("Enter Your Email: ")

has_space = False
has_uppercase = False
has_invalid_char = False

# Check minimum length
if len(email) >= 6:
    # Check if the first character is an alphabet
    if email[0].isalpha():
        # Check for exactly one "@" symbol
        if ("@" in email) and (email.count("@") == 1):
            # Check if the email ends with a proper domain
            if email[-4] == "." or email[-3] == ".":
                # Loop through each character in the email
                for char in email:
                    if char.isspace():  # Check for spaces
                        has_space = True
                    elif char.isalpha():  # Check for letters
                        if char.isupper():  # Uppercase letters
                            has_uppercase = True
                    elif char.isdigit():  # Allow digits
                        continue
                    elif char in "_@.":  # Allow _, @, .
                        continue
                    else:
                        has_invalid_char = True

                # Final validations based on flags
                if has_space:
                    print("Invalid Email: Email contains spaces.")
                elif has_uppercase:
                    print("Invalid Email: Email contains uppercase letters.")
                elif has_invalid_char:
                    print("Invalid Email: Email contains invalid characters.")
                else:
                    print("Valid Email!")
            else:
                print("Invalid Email: Email must end with a valid domain (e.g., .com or .org).")
        else:
            print("Invalid Email: Email must contain exactly one '@'.")
    else:
        print("Invalid Email: Email must start with a lowercase alphabet.")
else:
    print("Invalid Email: Email must be at least 6 characters long.")
