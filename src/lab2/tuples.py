def format_record(rec: tuple[str, str, float]) -> str:
    """
    This function takes tuple contains (fio, group, GPA) and returns str.

    Input data: tuple[str, str, float]

    Example: ("Иванов Иван Иванович", "BIVT-25", 4.6) --> Иванов И.И., гр. BIVT-25, GPA 4.60
    
    """
    # rec_list = list(rec)
    fio = rec[0].split()
    res = fio[0].capitalize() + ' '

    if rec[2] > 5 or rec[2]<0 or (type(rec[2]) != float and type(rec[2]) != int):
        raise ValueError("Incorrect GPA format")
    if fio == []:
        raise ValueError("Incorrect fio.")
    if rec[1] == '':
        raise ValueError("Incorrect group.")
    
    for i in range(1,len(fio)):
        res += (fio[i][0]).upper() + '.'
    res = f'{res}, гр. {rec[1]}, GPA {rec[2]:.2f}'
    return res


print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", 3.999) ))
print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", -1.999) ))
