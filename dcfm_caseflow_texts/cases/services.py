# Original path: cases/services.py


from django.utils import timezone

BASE_WEIGHTS = dict(urgency=8, age=1, public=10, deadline=12, complexity=2)

def compute_priority(case):
    age_days = (timezone.now().date() - case.filing_date).days
    deadline_bonus = 0
    if case.statutory_deadline:
        days_left = (case.statutory_deadline - timezone.now().date()).days
        deadline_bonus = max(0, 60 - days_left)  # simple proximity boost
    score = (
        BASE_WEIGHTS['urgency']*case.urgency_level +
        BASE_WEIGHTS['age']*age_days +
        BASE_WEIGHTS['public']*(1 if case.public_interest else 0) +
        BASE_WEIGHTS['deadline']*(1 if case.statutory_deadline else 0) +
        BASE_WEIGHTS['complexity']*case.complexity
    ) + deadline_bonus
    explain = [
        {"k":"urgency","v":case.urgency_level},
        {"k":"age_days","v":age_days},
        {"k":"public_interest","v":case.public_interest},
        {"k":"deadline","v":bool(case.statutory_deadline),"bonus":deadline_bonus},
        {"k":"complexity","v":case.complexity},
    ]
    return score, explain
