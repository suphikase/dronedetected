from matchingLine import matching_line

def quality(cell):
    quality = matching_line(cell, "Quality=").split()[0].split('/')
    return str(int(round(float(quality[0]) / float(quality[1]) * 100))).rjust(3) + " %"