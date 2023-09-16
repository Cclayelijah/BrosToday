from django.urls import path
from pushups import views

app_name = 'pushups'

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('test/<int:test_id>', views.test_result, name="test_result"),
    path('program/', views.program, name="program"),
    path('program/hard/', views.hard, name="hard"),
    path('program/extreme/', views.extreme, name="extreme"),
    path('program/impossible/', views.impossible, name="impossible"),
    path('progress/', views.progress, name="progress"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('workout/', views.workout, name="workout"),
    path('workout-form/<int:workout_type_id>', views.workout_form, name="workout_form"),
    path('workout-result/<int:workout_id>', views.workout_result, name="workout_result"),
]
