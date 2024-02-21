from PySide6.QtCore import Qt


def build_search_condition_by_column(model, search_value, selected_column):
    columns = [model.headerData(i, Qt.Horizontal) for i in range(model.columnCount())]
    conditions = [f"{selected_column} LIKE '%{search_value}%'" for _ in columns]
    return " OR ".join(conditions)
