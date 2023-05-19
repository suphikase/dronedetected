
from match import match
from matchingLine import matching_line

def encryption(cell):
    enc = ""
    if matching_line(cell, "Encryption key:") == "off":
        enc = "Open"
    else:
        for line in cell:
            matching = match(line, "IE:")
            if matching is not None:
                wpa = match(matching, "WPA Version ")
                if wpa is not None:
                    enc = "WPA v." + wpa
        if enc == "":
            enc = "WEP"
    return enc