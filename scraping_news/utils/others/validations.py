from datetime import datetime


def format_date_to_str(p_date: datetime):
    return str(p_date)[0:10].replace("-", "")


def format_datestr_to_date(p_date: str):
    new_date = p_date.replace("-", "")
    return datetime(int(new_date[0:4]), int(new_date[4:6]), int(new_date[6:8]))


def string_to_bool(string_value):
    if string_value.lower() == 'true':
        return True
    elif string_value.lower() == 'false':
        return False
    else:
        raise ValueError("A string não representa um valor booleano válido.")


def valid_input_date(p_date: str):
    try:
        datetime.fromisoformat(p_date)
        return True
    except Exception:
        return False


def valid_int(p_num):
    try:
        int(p_num)
        return True
    except ValueError:
        return False