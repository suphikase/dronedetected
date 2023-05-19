def average_signal_level(parsed_cells):
    total_signal_level = 0
    total_cells = len(parsed_cells)

    if total_cells == 0:
        return None

    for cell in parsed_cells:
        total_signal_level += int(cell['Signal'].split()[0])

    average_signal = round(total_signal_level / total_cells, 2)
    return average_signal