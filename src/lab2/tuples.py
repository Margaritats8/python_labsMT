def format_record(rec: tuple[str, str, float]) -> str:
    """
    This function takes tuple contains (fio, group, GPA) and returns str.

    Input data: tuple[str, str, float]

    Example: ("Иванов Иван Иванович", "BIVT-25", 4.6) --> Иванов И.И., гр. BIVT-25, GPA 4.60
    
    Raises:
    ValueError: Incorrect GPA format.
        When type of GPA isn't float/int or GPA not in 0 < GPA < 5.
    ValueError: Incorrect fio.
        Fio is empty.
    ValueError: Incorrect group.
        Group is empty.
    
    """
    fio, group, gpa = rec
    fio = fio.split()
    res = fio[0].capitalize() + ' '

    if gpa > 5 or gpa<0 or (type(gpa) != float and type(gpa) != int):
        raise ValueError("Incorrect GPA format")
    if fio == []:
        raise ValueError("Incorrect fio.")
    if group == '':
        raise ValueError("Incorrect group.")
    
    for i in range(1,len(fio)):
        res += (fio[i][0]).upper() + '.'
    res = f'{res}, гр. {group}, GPA {gpa:.2f}'
    return res


print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5) ))
print(format_record( ("  сИдОРова  анна   сергеевна ", "ABB-01", 3.999) ))
print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", -1.999) ))
