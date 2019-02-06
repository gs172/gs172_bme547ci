def is_tachycardic(str):
    if str == "tachycardic":
        return True
    elif str == "TACHYCARDIC":
        return True
    elif str == "Tachycardic":
        return True
    elif str == " tachycardic":
        return True
    elif str == "tachycardic ":
        return True
    elif str == "tachycardic.":
        return True
    elif str == "Tachycardic.":
        return True
    elif str == "Tachycardic ":
        return True
    elif str == " Tachycardic":
        return True
    elif str == " Tachycardic.":
        return True
    elif str == "TACHYCARDIC ":
        return True
    elif str == " TACHYCARDIC":
        return True
    elif str == " TACHYCARDIC.":
        return True
    elif str == "TACHYCARDIC.":
        return True
    else:
        return False


def runcode():
    inp = input("Please enter the word 'tachycardic:' ")
    print(is_tachycardic(inp))

if __name__ == "__main__":
    runcode()
