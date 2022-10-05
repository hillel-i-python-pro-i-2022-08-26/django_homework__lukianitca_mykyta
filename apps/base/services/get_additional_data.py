from string import ascii_letters, digits


def get_safe_chars() -> list:
    return list(ascii_letters + digits + "_")
