def calculate_fine(days_overdue, book_type):
    rates = {"standard": 2.0, "reference": 5.0, "rare": 10.0}
    if days_overdue is None or not isinstance(days_overdue, (int, float)) or days_overdue < 0:
        return 0.0
    if book_type is None or not isinstance(book_type, str):
        book_type_key = "standard"
    else:
        book_type_key = book_type.strip().lower()
    rate = rates.get(book_type_key, rates["standard"])
    return float(days_overdue * rate)

def calculate_total_bill(fines_list):
    if fines_list is None or not isinstance(fines_list, (list, tuple)):
        return 0.0
    total = 0.0
    for fine in fines_list:
        if isinstance(fine, (int, float)) and fine >= 0:
            total += float(fine)
    return total

def parse_overdue_days(days_input):
    if days_input is None:
        return 0
    if isinstance(days_input, (int, float)):
        return max(0, int(days_input))
    if isinstance(days_input, str):
        cleaned = days_input.strip()
        if not cleaned:
            return 0
        try:
            return max(0, int(cleaned))
        except ValueError:
            return 0
    return 0

