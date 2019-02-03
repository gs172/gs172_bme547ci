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
