def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False