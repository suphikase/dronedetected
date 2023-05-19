from matchingLine import matching_line

def signal_level(cell):
    return matching_line(cell, "Quality=").split("Signal level=")[1]