# Restriction:
# 1. Must be between 2 to 6 characters
# 2. The first 2 characters must be letters
# 3. Must only contain alphanumeric characters
# 4. You can't have numbers in between Letters
# 5. You can't have an 0 start a group or numbers

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        elif s[:2].isalpha():
            if len(s) == 3:
                return True
            elif s[-1].isalpha():
                for _ in s:
                    if _.isnumeric():
                        return False
            elif s[-1].isnumeric():
                for _ in s:
                    if _.isnumeric():
                        if _ == "0":
                            return False
                        else:
                            return True
            # return True
        else:
            return False
    else:
        return False
    
def main():
    plates = input("Enter your vanity plate: ")
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()