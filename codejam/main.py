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

    top_border = '┬'.join(['─' * length for length in cols_length])
    result += '┌' + top_border + '┐'

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
    print(len('┌────────────┬───────────┬─────────┐'))
    print(table)