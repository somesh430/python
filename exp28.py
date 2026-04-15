values = ['a', 0, 2, 'a', 0, 2]
for val in values:
    try:
        print("The entry is", val)
        num = int(val)            
        result = 1 / num            
    except Exception as e:
        print("Oops!", type(e), "occurred.")
        print("Next entry.")
    else:
        print("The reciprocal of", num, "is", result)
