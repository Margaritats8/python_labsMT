def format_record(rec: tuple):
    rec_list = list(rec)
    el1 = rec_list[0].split()
    res = el1[0].capitalize() + ' '
    if rec_list[2] > 5 or rec_list[2]<0:
        return ValueError
    for i in range(1,len(el1)):
        res += (el1[i][0]).upper() + '.'
    res = f'{res}, гр. {rec_list[1]}, GPA {rec_list[2]:.2f}'
    return res

print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))