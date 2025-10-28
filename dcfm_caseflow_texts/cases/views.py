# Original path: cases/views.py


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Case
from .forms import CaseForm
from .services import compute_priority
from scheduling.models import TimeStandard, Bench, ScheduleSlot
from datetime import timedelta

def home(request):
    return render(request, 'home.html')

def case_list(request):
    cases = Case.objects.all().select_related('bench_assigned')
    return render(request, 'cases/list.html', {'cases': cases})

def case_create(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            messages.success(request, 'Case created.')
            return redirect('case_detail', pk=case.id)
    else:
        form = CaseForm()
    return render(request, 'cases/create.html', {'form': form})

def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    explain = None
    if case.priority_explain:
        import json
        explain = json.dumps(case.priority_explain, indent=2, default=str)
    return render(request, 'cases/detail.html', {'case': case, 'explain': explain})

def compute_priority_view(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        score, explain = compute_priority(case)
        case.priority_score = score
        case.priority_explain = explain
        case.save(update_fields=['priority_score','priority_explain'])
        messages.success(request, f'Priority computed: {score}')
    return redirect('case_detail', pk=pk)

def auto_schedule_view(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        # find SLA window
        ts = TimeStandard.objects.filter(case_type=case.case_type, category=case.category).first()
        sla_days = ts.first_listing_days if ts else 30
        start = timezone.now().date()
        end = start + timedelta(days=sla_days)

        benches = Bench.objects.all()
        day = start
        assigned = False
        while day <= end and not assigned:
            for bench in benches:
                slot = ScheduleSlot.objects.filter(bench=bench, date=day, allocated_case__isnull=True).order_by('start_time').first()
                if slot:
                    slot.allocated_case = case
                    slot.save()
                    case.state = 'LISTED'
                    case.bench_assigned = bench
                    case.next_hearing_date = day
                    case.save(update_fields=['state','bench_assigned','next_hearing_date'])
                    messages.success(request, f'Case listed on {day} at {bench.name}.')
                    assigned = True
                    break
            day += timedelta(days=1)
        if not assigned:
            messages.error(request, 'No free slot within SLA window.')
    return redirect('case_detail', pk=pk)
