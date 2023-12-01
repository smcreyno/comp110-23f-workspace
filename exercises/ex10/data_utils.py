"""Dictionary related utility functions."""

__author__ = "730642974"

from csv import DictReader


def read_csv_rows(data_file_path: str) -> list[dict[str, str]]:
    """Read CSV file and return the rows into a list; each row is a dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(data_file_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Produce a list of strings of all values in a single column whose name is 'key'."""
    result: list[str] = []
    for elem in table:
        result.append(elem[key])
    return result


def columnar(list_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table of a list of rows into one of a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = list_table[0]
    for key in first_row:
        result[key] = column_values(list_table, key)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if num_rows >= len(table):
        return table
    for col in table:
        storage: list[str] = []
        for row in range(0, num_rows):
            val: list[str] = table[col]
            storage.append(val[row])
        result[col] = storage
    return result


def select(table: dict[str, list[str]], col_name: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for col in table:
        if col in col_name:
            val: list[str] = table[col]
            result[col] = val
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table by combining two tables."""
    result: dict[str, list[str]] = {}
    for col in table1:
        result[col] = table1[col]
    for umn in table2:
        if umn in result:
            result[umn] += table2[umn]
        else:
            result[umn] = table2[umn]
    return result


def count(vals: list[str]) -> dict[str, int]:
    """Given vals, count produces a dict where each key is a unique val and has the count of the number of times it appears."""
    result: dict[str, int] = {}
    for elem in vals:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result