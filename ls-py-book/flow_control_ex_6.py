def caps_if_long(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str
    
print(caps_if_long('ggg'))