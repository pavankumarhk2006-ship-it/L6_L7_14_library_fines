
import pytest
from library_fines import late_fine, can_borrow, renewal_status


# =====================================
# CODE COVERAGE TEST CASES
# =====================================

# 1. Late Fine Tests

def test_returned_on_time():
    assert late_fine("student", 10, False) == 0

def test_student_overdue():
    assert late_fine("student", 15, False) == 2

def test_faculty_overdue():
    assert late_fine("faculty", 31, False) == 1

def test_guest_overdue():
    assert late_fine("guest", 15, False) == 5

def test_faculty_on_time():
    assert late_fine("faculty", 30, False) == 0

def test_fine_capped():
    assert late_fine("student", 115, False) == 200

def test_damaged_book():
    assert late_fine("student", 10, True) == 150

def test_overdue_damaged_book():
    assert late_fine("student", 20, True) == 162

def test_unknown_member():
    with pytest.raises(ValueError):
        late_fine("visitor", 10, False)

def test_negative_days():
    with pytest.raises(ValueError):
        late_fine("student", -1, False)


# 2. Can Borrow Tests

def test_student_can_borrow():
    assert can_borrow(1, 0, "student") is True

def test_pending_fine_exceeds_limit():
    assert can_borrow(1, 101, "student") is False

def test_fine_at_limit():
    assert can_borrow(1, 100, "student") is True

def test_faculty_can_borrow():
    assert can_borrow(9, 0, "faculty") is True

def test_faculty_limit():
    assert can_borrow(10, 0, "faculty") is False

def test_student_limit():
    assert can_borrow(3, 0, "student") is False

def test_guest_can_borrow():
    assert can_borrow(2, 0, "guest") is True

def test_guest_limit():
    assert can_borrow(3, 0, "guest") is False


# 3. Renewal Status Tests

def test_reservation_denied():
    assert renewal_status(0, True, 10) == "denied"

def test_renewal_limit():
    assert renewal_status(2, False, 10) == "limit reached"

def test_renewal_limit_exceeded():
    assert renewal_status(3, False, 10) == "limit reached"

def test_overdue_renewal():
    assert renewal_status(1, False, -1) == "overdue"

def test_successful_renewal():
    assert renewal_status(0, False, 10) == "renewed"

def test_renewal_last_day():
    assert renewal_status(1, False, 0) == "renewed"
