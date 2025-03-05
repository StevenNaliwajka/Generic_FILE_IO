def format_csv_entry(dict_of_items: dict) -> str:
    """Formats dictionary items for CSV by replacing commas in values with underscores."""
    if not isinstance(dict_of_items, dict):
        raise TypeError(f"Expected a dictionary, got {type(dict_of_items)}: {dict_of_items}")

    formatted_values = [str(value).replace(',', '_') for value in dict_of_items.values()]

    return ','.join(formatted_values)