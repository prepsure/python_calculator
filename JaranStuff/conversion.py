from input_handler import __input_eval as enput


def temperature_converter():
    return {
        "c to f": lambda x: x * (9 / 5) + 32,
        "f to c": lambda x: (x - 32) * (5 / 9),
        "c to k": lambda x: x + 273.15,
        "k to c": lambda x: x - 273.15,
        "f to k": lambda x: (x - 32) * (5 / 9) + 273.15,
        "k to f": lambda x: (x - 273.15) * (9 / 5) + 32
    }[enput("Enter Start:", str).lower()[0] + " to " + enput("Enter Find:", str).lower()[0]](enput("Enter Value:", float))


def unit_conversion(unit=None, start=None, to=None, val=None):
    unit = enput("Enter Unit of Conversion:", str).lower() if not unit else unit
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
    start = enput("Enter From:", str).lower() if not start else start
    to = enput("Enter To:", str).lower() if not to else to
    val = enput("Enter Value:", float) if not val else val
    return (lambda f, t, v: v * 10 ** (
            sum(v for k, v in get_power.items() if f in k) -
            sum(v for k, v in get_power.items() if t in k)))(start, to, val)


def time_conversion():
    start = enput("Enter Start:", str).lower()
    to = enput("Enter To:", str).lower()
    val = enput("Enter Value:", float)
    conversion_rate = {
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
        return seconds * (1/sum(v for k, v in conversion_rate.items() if __contains(k, to)))
    else:
        seconds = val * sum(v for k, v in conversion_rate.items() if __contains(k, start))
        return unit_conversion(unit="s", start="s", to=to, val=seconds)


def __contains(lst, string):
    return sum([x in string for x in lst]) != 0
