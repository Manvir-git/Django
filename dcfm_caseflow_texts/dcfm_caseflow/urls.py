# Original path: dcfm_caseflow/urls.py


from django.contrib import admin
from django.urls import path
from cases.views import home, case_list, case_create, case_detail, compute_priority_view, auto_schedule_view
from reports.views import cause_list_api, cause_list_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cases/', case_list, name='case_list'),
    path('cases/new/', case_create, name='case_create'),
    path('cases/<int:pk>/', case_detail, name='case_detail'),
    path('cases/<int:pk>/compute-priority/', compute_priority_view, name='compute_priority'),
    path('cases/<int:pk>/auto-schedule/', auto_schedule_view, name='auto_schedule'),
    path('api/reports/cause-list', cause_list_api, name='cause_list_api'),
    path('reports/cause-list', cause_list_page, name='cause_list_page'),
]
