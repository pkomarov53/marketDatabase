from PySide6.QtCore import Qt


def build_search_condition_by_value(model, selected_column, search_value):
    if selected_column == "all_columns":
        columns = [model.headerData(i, Qt.Horizontal) for i in range(model.columnCount())]
        conditions = [f"{column} LIKE '%{search_value}%'" for column in columns]
        return " OR ".join(conditions)
    else:
        return f"{selected_column} LIKE '%{search_value}%'"
