def format_record(rec: tuple[str, str, float]) -> str:
    """
    
    
    
    """
    rec_list = list(rec)
    fio = rec_list[0].split()
    print(fio)
    res = fio[0].capitalize() + ' '
    if rec_list[2] > 5 or rec_list[2]<0:
        raise ValueError("Incorrect GPA format")
    for i in range(1,len(fio)):
        res += (fio[i][0]).upper() + '.'
    res = f'{res}, гр. {rec_list[1]}, GPA {rec_list[2]:.2f}'
    return res


print(format_record( ("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record( ("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record( ("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record( ("  сидОрова  анна   сергеевна ", "ABB-01", 3.999) ))
print(format_record( ("  сиДорова  анна   сергеевна ", "ABB-01", -1.999) ))
