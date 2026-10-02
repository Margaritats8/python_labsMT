def format_record(rec: tuple[str, str, float]) -> str:
    """
    This function takes tuple contains (fio, group, GPA) and returns str.

    Input data: tuple[str, str, float]

    Example: ("Иванов Иван Иванович", "BIVT-25", 4.6) --> Иванов И.И., гр. BIVT-25, GPA 4.60
    
    Raises:
    ValueError: Incorrect GPA format.
        When type of GPA isn't float/int or GPA not in 0 < GPA < 5.
    ValueError: Incorrect group.
        Group is empty.
    ValueError: Incorrect tuple size.
        Tuple must contain exactly 3 elements.
    TypeError: Input is not a tuple.
        Input data must be a tuple.
    TypeError: Incorrect type of fio
        Input data must be string and include 2 or 3 words.
    TypeError: Fio includes only alfa.
        The symbols in the full name are not letters.
    """
    if type(rec) != tuple:
        raise TypeError(f"Input data must be a tuple, but got {type(rec)}")
    
    if len(rec) != 3:
        raise ValueError(f"Tuple must contain exactly 3 elements, but got {len(rec)}")

    fio, group, gpa = rec

    if type(fio) == str:
        fio = fio.split()
    else:
        raise TypeError('Incorrect type of fio')
    
    for j in fio:
            if not j.replace('-','').isalpha():
                raise TypeError('fio includes only alfa')
            
    if  2 <= len(fio) <=3:
        res = fio[0].capitalize() + ' '
    else:
        raise TypeError('Incorrect type of fio')
    

    if gpa > 5 or gpa < 0 or (type(gpa) != float and type(gpa) != int):
        raise ValueError("Incorrect GPA format")

    if group == '' or type(group) != str:
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
