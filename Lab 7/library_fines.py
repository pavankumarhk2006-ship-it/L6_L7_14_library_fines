def parse_member_id(member_id):
    """Safely parses member ID with strict validation."""
    if not isinstance(member_id, str) or '-' not in member_id:
        return ("UNKNOWN", 0)
    parts = member_id.split('-')
    if len(parts) != 2 or not parts[1].strip().isdigit():
        return (parts[0].upper() if parts[0] else "UNKNOWN", 0)
    return parts[0].upper(), int(parts[1].strip())

def total_fine(days_csv):
    """Safely calculates total fine from CSV string."""
    if not isinstance(days_csv, str) or not days_csv.strip():
        return 0
    fine = 0
    for d in days_csv.split(','):
        d_clean = d.strip()
        if d_clean.isdigit():
            val = int(d_clean)
            if val > 14:
                fine += (val - 14) * 2
    return fine

def shelf_code(title):
    """Safely generates a shelf code from a book title."""
    if not isinstance(title, str) or not title.strip():
        return "XX"
    words = title.split()
    if len(words) < 2:
        return "XX"
    return (words[0][0] + words[1][0]).upper()

def main():
    print("==== Running parse_member_id ====")
    user_input = input("Enter a member ID (e.g. STU-1023): ")
    result = parse_member_id(user_input)
    print("Member Type and Number:", result)

    print("\n==== Running total_fine ====")
    user_input = input("Enter days kept for each book as CSV (e.g. 10,20,30): ")
    result = total_fine(user_input)
    print("Total Fine:", result)

    print("\n==== Running shelf_code ====")
    user_input = input("Enter a book title with at least two words: ")
    result = shelf_code(user_input)
    print("Shelf Code:", result)

if __name__ == "__main__":
    main()