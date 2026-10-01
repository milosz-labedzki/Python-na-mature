def odwroc(s):
    s = s[::-1]
    return s



assert odwroc("matura") == "arutam"
assert odwroc("a") == "a"
assert odwroc("") == ""