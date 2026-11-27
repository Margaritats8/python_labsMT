from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def check_text(value, name):
    """fio and group: must be a string, non-empty after strip(). Returns the stripped string."""
    if not isinstance(value, str):
        raise ValueError(f"field {name}: expected a string")
    value = value.strip()
    if value == "":
        raise ValueError(f"field {name}: string must not be empty")
    return value


def check_birthdate(value):
    """birthdate: string in YYYY-MM-DD format, a real date, not in the future."""
    if not isinstance(value, str):
        raise ValueError("field birthdate: expected a string in YYYY-MM-DD format")
    try:
        d = date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"field birthdate: '{value}' is a non-existent date or is not in YYYY-MM-DD format")
    if d > date.today():
        raise ValueError(f"field birthdate: date '{value}' is in the future")
    return value


def check_gpa(value):
    """gpa: int or float, 0 <= gpa <= 5. Returns a float."""
    if not isinstance(value, (int, float)):
        raise ValueError("field gpa: expected a number (int or float)")
    if not (0 <= value <= 5):
        raise ValueError(f"field gpa: value {value} is out of range 0..5")
    return float(value)


def make_student(fio, birthdate, group, gpa):
    """Builds a student record, validating each field.

    make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-1", 4.3)
    """
    return {
        "fio": check_text(fio, "fio"),
        "birthdate": check_birthdate(birthdate),
        "group": check_text(group, "group"),
        "gpa": check_gpa(gpa),
    }


def validate_student(rec):
    """Validates a complete record: key set and values. Raises ValueError on error."""
    if not isinstance(rec, dict):
        raise ValueError("Record must be a dictionary")
    if set(rec) != set(STUDENT_FIELDS):
        missing = set(STUDENT_FIELDS) - set(rec)
        extra = set(rec) - set(STUDENT_FIELDS)
        raise ValueError(f"invalid key set: missing {sorted(missing)}, extra {sorted(extra)}")
    check_text(rec["fio"], "fio")
    check_birthdate(rec["birthdate"])
    check_text(rec["group"], "group")
    check_gpa(rec["gpa"])


def student_age(rec, today=None):
    """Full years of age on the given date (today by default)."""
    b = date.fromisoformat(rec["birthdate"])

    if isinstance(today, str):
        today = date.fromisoformat(today)
    elif today == None:
        today = date.today()
    elif not isinstance(today, date):
        raise ValueError("Today must be date, string or None")
    age = today.year - b.year
    if (today.month, today.day) < (b.month, b.day): 
        age -= 1
    return age


def years_word(n):
    """Correct word form: 1 год, 2 года, 5 лет."""
    if 11 <= n % 100 <= 14:
        return "лет"
    if n % 10 == 1:
        return "год"
    if 2 <= n % 10 <= 4:
        return "года"
    return "лет"


def format_student(rec):
    """Иванов И.И. (БИВТ-26-6-1), 19 лет, GPA 4.30"""
    parts = rec["fio"].split()
    initials = "".join(p[0].upper() + "." for p in parts[1:3])
    name = parts[0] + (" " + initials if initials else "")
    age = student_age(rec)
    return f"{name} ({rec['group']}), {age} {years_word(age)}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec):
    """Copy of the record (not the same dictionary) for serialization."""
    validate_student(rec)
    return {key: rec[key] for key in STUDENT_FIELDS}


def student_from_dict(d):
    """Deserialization: takes exactly the required keys, make gpa to float, validates."""
    if not isinstance(d, dict):
        raise ValueError("Record must be an object (dictionary)")
    for key in STUDENT_FIELDS:
       if key not in d:
          raise ValueError(f"missing field {key}")
    return make_student(d["fio"], d["birthdate"], d["group"], d["gpa"])


def main():
    s = make_student("Цапкова Маргарита Александровна", "2008-03-12", "БИВТ-26-6-2", 5)
    print("Создан студент:", s)
    
    print("Форматирование:", format_student(s))

    print(student_age(s, date(2026, 3, 11)), student_age(s, date(2026, 3, 12)))

    for args in (("Васильев Василий Васильевич", "2000-01-32", "БИВТ-26-6-1", 4.0),
                 ("Андреев Андрей Андреевич", "2005-03-19", "БИВТ-26-6-1", 7),
                 ("Иванов Иван Иванович","2008-05-01","БИВТ-26-6-2", "4" )):
        try:
            make_student(*args)
        except ValueError as e:
            print("ValueError:", e)

if __name__ == "__main__":
    main()