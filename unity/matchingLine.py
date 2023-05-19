from match import match

def matching_line(lines, keyword):
    for line in lines:
        matching = match(line, keyword)
        if matching is not None:
            return matching
    return None