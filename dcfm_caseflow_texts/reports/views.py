# Original path: reports/views.py


from django.http import JsonResponse
from django.shortcuts import render
from cases.models import Case

def cause_list_api(request):
    date = request.GET.get('date')
    qs = Case.objects.filter(state='LISTED')
    if date:
        qs = qs.filter(next_hearing_date=date)
    data = {}
    for c in qs.select_related('bench_assigned'):
        bench = c.bench_assigned.name if c.bench_assigned else 'Unassigned'
        data.setdefault(bench, []).append({
            'case': c.number,
            'type': c.case_type,
            'category': c.category,
            'date': str(c.next_hearing_date),
            'priority': c.priority_score,
        })
    return JsonResponse(data)

def cause_list_page(request):
    date = request.GET.get('date')
    qs = Case.objects.filter(state='LISTED')
    if date:
        qs = qs.filter(next_hearing_date=date)
    data = {}
    for c in qs.select_related('bench_assigned'):
        bench = c.bench_assigned.name if c.bench_assigned else 'Unassigned'
        data.setdefault(bench, []).append({
            'case': c.number,
            'type': c.case_type,
            'category': c.category,
            'date': str(c.next_hearing_date),
            'priority': c.priority_score,
        })
    return render(request, 'reports/cause_list.html', {'data': data, 'date': date})
