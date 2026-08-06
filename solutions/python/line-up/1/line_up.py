
def line_up(name, number):
    ns = str(number)[-1]
    endNumber = "st" if ns == "1" else ("nd" if ns == "2" else ( "rd" if ns == "3" else "th") )
    ns2 = str(number)[-2:]
    if ns2 == "11" or ns2 == "12" or ns2 == "13":
        endNumber = "th"
    return f"{name}, you are the {number}{endNumber} customer we serve today. Thank you!"
