def standard_deviation_signal_level(parsed_cells, average_signal):
    if len(parsed_cells) == 0:
        return None

    variance = sum([(int(cell['Signal'].split()[0]) - average_signal) ** 2 for cell in parsed_cells]) / len(parsed_cells)
    std_dev = round(variance ** 0.5, 2)
    return std_dev, average_signal