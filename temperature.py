def isoverheating(temp_c):
    if temp_c < 0:
        raise ValueError("Reading error")
    return temp_c > 80