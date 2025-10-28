# Original path: cases/models.py


from django.db import models
from django.utils import timezone


class Case(models.Model):
    CASE_TYPES = [('CIVIL','Civil'),('CRIMINAL','Criminal'),('WRIT','Writ'),('TAX','Tax'),('OTHER','Other')]
    CATEGORY = [('SUMMARY','Summary'),('REGULAR','Regular'),('COMPLEX','Complex')]
    STATES = [('DRAFT','Draft'),('FILED','Filed'),('ADMITTED','Admitted'),('LISTED','Listed'),
              ('HEARD','Heard'),('ORDER_RESERVED','Order Reserved'),('DISPOSED','Disposed'),('REJECTED','Rejected')]

    number = models.CharField(max_length=32, unique=True)
    year = models.PositiveIntegerField()
    case_type = models.CharField(max_length=16, choices=CASE_TYPES)
    category = models.CharField(max_length=16, choices=CATEGORY, default='REGULAR')
    complexity = models.PositiveSmallIntegerField(default=2)  # 1..5
    urgency_level = models.PositiveSmallIntegerField(default=1)  # 1..5
    public_interest = models.BooleanField(default=False)
    statutory_deadline = models.DateField(null=True, blank=True)

    priority_score = models.IntegerField(default=0)
    priority_explain = models.JSONField(default=list, blank=True)

    state = models.CharField(max_length=16, choices=STATES, default='DRAFT')
    filing_date = models.DateField(default=timezone.now)
    admitted_date = models.DateField(null=True, blank=True)
    next_hearing_date = models.DateField(null=True, blank=True)

    bench_assigned = models.ForeignKey(
        'scheduling.Bench',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='cases',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority_score','filing_date']

    def __str__(self):
        return self.number


class Party(models.Model):
    ROLES = [('PETITIONER','Petitioner'),('RESPONDENT','Respondent'),('INTERVENOR','Intervenor')]
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='parties')
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=16, choices=ROLES)
    advocate = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.role}: {self.name}"
