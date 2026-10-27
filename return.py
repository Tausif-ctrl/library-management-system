# return.py
from datetime import date

FINE_PER_DAY = 5

def return_book(book_id, member_id, due_date, return_date):
    overdue_days = (return_date - due_date).days
    if overdue_days > 0:
        fine = overdue_days * FINE_PER_DAY
        print(f"Book {book_id} returned. Late by {overdue_days} days. Fine = {fine}")
        return fine
    else:
        print(f"Book {book_id} returned on time. No fine.")
        return 0

if __name__ == "__main__":
    return_book(101, 2001, date(2025, 1, 10), date(2025, 1, 15))
