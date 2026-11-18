from hypothesis import given, strategies as st
import pytest
from processor import calculate_fine, calculate_total_bill, parse_overdue_days

@given(
    days_overdue=st.integers() | st.none(),
    book_type=st.text() | st.none()
)
def test_calculate_fine_no_crash(days_overdue, book_type):
    try:
        calculate_fine(days_overdue, book_type)
    except Exception as e:
        assert False, f"calculate_fine crashed with: {type(e).__name__}: {e}"

@given(
    fines_list=st.lists(st.floats(allow_nan=False, allow_infinity=False)) | st.none()
)
def test_calculate_total_bill_no_crash(fines_list):
    try:
        calculate_total_bill(fines_list)
    except Exception as e:
        assert False, f"calculate_total_bill crashed with: {type(e).__name__}: {e}"

@given(
    days_input=st.text() | st.integers() | st.none()
)
def test_parse_overdue_days_no_crash(days_input):
    try:
        parse_overdue_days(days_input)
    except Exception as e:
        assert False, f"parse_overdue_days crashed with: {type(e).__name__}: {e}"

