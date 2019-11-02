def temperature_converter():
    return {
        "c to f": lambda x: x * (9 / 5) + 32,
        "f to c": lambda x: (x - 32) * (5 / 9),
        "c to k": lambda x: x + 273.15,
        "k to c": lambda x: x - 273.15,
        "f to k": lambda x: (x - 32) * (5 / 9) + 273.15,
        "k to f": lambda x: (x - 273.15) * (9 / 5) + 32
    }[input("Enter Start: ").lower()[0] + " to " + input("Enter Find: ").lower()[0]](float(input("Enter Value: ")))


def unit_conversion(unit=None, start=None, to=None, val=None):
    unit = input("Enter Unit of Conversion: ").lower() if not unit else unit
    get_power = {
        ("exa" + unit, "E" + unit[0]): 18,
        ("peta" + unit, "P" + unit[0]): 15,
        ("tera" + unit, "T" + unit[0]): 12,
        ("giga" + unit, "G" + unit[0]): 9,
        ("mega" + unit, "M" + unit[0]): 6,
        ("kilo" + unit, "k" + unit[0]): 3,
        ("hecto" + unit, "h" + unit[0]): 2,
        ("deka" + unit, "da" + unit[0]): 1,
        (unit, "", unit[0]): 0,
        ("deci" + unit, "d" + unit[0]): -1,
        ("centi" + unit, "c" + unit[0]): -2,
        ("milli" + unit, "m" + unit[0]): -3,
        ("micro" + unit, "u" + unit[0]): -6,
        ("nano" + unit, "n" + unit[0]): -9,
        ("pico" + unit, "p" + unit[0], "micro micro" + unit, "uu" + unit[0]): -12,
        ("femto" + unit, "f" + unit[0]): -15,
        ("atto" + unit, "a" + unit[0]): -18
    }
    return (lambda f, t, V: V * 10 ** (
                sum(v for k, v in get_power.items() if f in k) - sum(v for k, v in get_power.items() if t in k)))(
        input("Enter From: ").lower() if not start else start, input("Enter To: ").lower() if not to else to,
        float(input("Enter Value: ")) if not val else val)


def time_conversion():
    start = input("Enter Start: ").lower()
    to = input("Enter To: ").lower()
    val = float(input("Enter Value: "))
    conv_rate = {
        ("m", "min", "minute"): 60,
        ("h", "hr", "hour"): 3600,
        ("d", "day"): 86400,
        ("w", "wk", "week"): 604800,
        ("M", "month"): 2.628e+6,
        ("y", "year"): 3.154e+7,
        ("D", "dec", "decade"): 3.154e+8,
        ("c", "cent", "century"): 3.154e+9
    }
    if __contains(["s", "sec", "second"], start) and __contains(["s", "sec", "second"], to):
        return unit_conversion(unit="s", start=start, to=to, val=val)
    elif __contains(["s", "sec", "second"], start):
        seconds = unit_conversion(unit="s", start=start, to="s", val=val)
        return seconds * (1 / sum(v for k, v in conv_rate.items() if __contains(k, to)))
    else:
        seconds = val * sum(v for k, v in conv_rate.items() if __contains(k, start))
        return unit_conversion(unit="s", start="s", to=to, val=seconds)


def __contains(lst, string):
    return sum([x in string for x in lst]) != 0