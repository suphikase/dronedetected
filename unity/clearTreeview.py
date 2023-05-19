def clear_treeview(tree):
    for item in tree.get_children():
        tree.delete(item)