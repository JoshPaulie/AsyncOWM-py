def pretty_temp(temp: int, unit: str = "imperial") -> str:
    # todo C, other
    symbol = None
    if unit == "imperial":
        symbol = "F"
    temp = round(temp)
    temp_str = f"{str(temp)}°{symbol}"
    return temp_str
