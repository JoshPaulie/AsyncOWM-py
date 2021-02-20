from .data_enums import Unit


def pretty_temp(temp: int, unit: Unit) -> str:
    symbol = unit.value[0]
    temp = round(temp)
    temp_str = f"{str(temp)}°{symbol}"
    return temp_str
