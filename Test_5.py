def compare_versions(ver_1, ver_2):
    try:
        list_ver_1 = ver_1.split(".")
    except:
        list_ver_1 = repr(ver_1)

    try:
        list_ver_2 = ver_2.split(".")
    except:
        list_ver_2 = repr(ver_2)

    result = 0
    min_len = min(list_ver_1, list_ver_2, key=len)
    for i in range(len(min_len)):
        part_diff = int(list_ver_1[i]) - int(list_ver_2[i])
        if part_diff:
            result = part_diff
            break

    if result == 0: result = len(list_ver_1) - len(list_ver_2)

    if result > 0:
        result = 1
    elif result < 0:
        result = -1

    return result
