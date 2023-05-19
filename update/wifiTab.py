from unity.clearTreeview import clear_treeview


columns = ["Name", "Quality", "Channel", "Encryption", "Address", "Signal"] 

def update_wifi_tab(parsed_cells):
    global tree
    
    clear_treeview(tree)
    table_data = [list(cell[column] for column in columns) for cell in parsed_cells]
    for row in table_data:
        tree.insert("", "end", values=row)