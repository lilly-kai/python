#already given
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # All vanity plates must start with at least two letters.
    if not s[0:2].isalpha():
        return False

    # maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            return s[i:].isdigit()

    # "No periods, spaces, or punctuation marks are allowed."
    if not s.isalnum():
        return False

    return True


main()
