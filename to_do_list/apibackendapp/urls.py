from django.urls import path
from .views import SignupView, LoginView, TaskListCreateView, TaskDetailView

urlpatterns = [
    # Auth
    path("api/users/signup/", SignupView.as_view(), name="signup"),
    path("api/users/login/", LoginView.as_view(), name="login"),

    # Tasks
    path("api/tasks/", TaskListCreateView.as_view(), name="task-list"),
    path("api/tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
