def sort_cells(cells):
    cells.sort(key=lambda el: el["Quality"], reverse=True)