from django.urls import path
from .views import OffspringListView, OffspringCreateView, OffspringDeleteView, OffspringUpdateView, OffspringAssignmentNew, OffspringAssignmentCreate


app_name = 'offsprings'
urlpatterns = [
    path('', OffspringListView.as_view(), name='index'),
    path('create', OffspringCreateView.as_view(), name='create'),
    path('<int:pk>/update', OffspringUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', OffspringDeleteView.as_view(), name='delete'),
    path('<int:pk>/assign', OffspringAssignmentNew.as_view(), name='assign'),
    path('<int:offspring_id>/<int:schedule_id>/assign',
         OffspringAssignmentCreate.as_view(), name='createassignment')
]
