def nearly_equal(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    i = j = 0
    count = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            count += 1
            if count > 1:
                return False
            if len(str1) > len(str2):
                i += 1
                continue
            elif len(str1) < len(str2):
                j += 1
                continue
        else:
            i += 1
            j += 1

    return True
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if nearly_equal(s1, s2):
    print("Strings are nearly equal")
else:
    print("Strings are NOT nearly equal")
