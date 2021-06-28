from typing import List, Optional, Any

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    result = ''

    if labels is None:
        labels_n_rows = rows
    else:
        labels_n_rows = [labels] + rows

    cols_length = [0] * len(labels_n_rows[0])
    for item in labels_n_rows:
        length = [len(str(val)) + 2 for val in item]
        for index, val in enumerate(zip(cols_length, length)):
            if val[0] > val[1]:
                cols_length[index] = val[0]
            else:
                cols_length[index] = val[1]

    border_top = '┬'.join(['─' * length for length in cols_length])
    result += '┌' + border_top + '┐' + '\n'

    for index, row in enumerate(labels_n_rows):
        if labels is not None and index == 0:
            if centered:
                row_of_strings = [str(item).center(cols_length[ind], ' ') for ind, item in enumerate(row)]
            else:
                row_of_strings = [f' {item:<{cols_length[ind] - 2}} ' for ind, item in enumerate(row)]
            joined = '│'.join(row_of_strings)
            result += '│' + joined + '│' + '\n'
            border_label = '┼'.join(['─' * length for length in cols_length])
            result += '├' + border_label + '┤' + '\n'
            continue
        if centered:
            row_of_strings = [str(item).center(cols_length[ind], ' ') for ind, item in enumerate(row)]
        else:
            row_of_strings = [f' {item:<{cols_length[ind] - 2}} ' for ind, item in enumerate(row)]
        joined = '│'.join(row_of_strings)
        result += '│' + joined + '│' + '\n'

    border_bottom = '┴'.join(['─' * length for length in cols_length])
    result += '└' + border_bottom + '┘' + '\n'

    return result



if __name__ == '__main__':
    table = make_table(
        rows=[
            ["Lemon", 18_3285, "Owner"],
            ["Sebastiaan", 18_3285.1, "Owner"],
            ["KutieKatj", 15_000, "Admin"],
            ["Jake", "MoreThanU", "Helper"],
            ["Joe", -12, "Idk Tbh"]
        ],
        labels=["User", "Messages", "Role"]
    )

    print(table)