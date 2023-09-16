from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Workout, WorkoutType, BenchmarkTest
from .forms import TestForm, WorkoutForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView
from datetime import datetime, timedelta


class UserListView(ListView):
    paginate_by = 2
    model = Profile


def index(request):
    return render(request, 'index.html')


@login_required
def progress(request):
    context = {}
    context['test_data'] = BenchmarkTest.objects.filter(user=request.user)
    context['workout_data'] = Workout.objects.filter(user=request.user)
    return render(request, 'progress.html', context)


@login_required
def test(request):
    context = {}
    form = TestForm(request.POST or None)
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            pushups = form.cleaned_data.get("pushups")

            record = BenchmarkTest(user=User.objects.get(username=request.user.username), pushups=pushups)
            record.save()
            profile = Profile.objects.get(user_id=request.user.id)
            profile.total_pushups = profile.total_pushups + pushups
            profile.save()
            return redirect('pushups:test_result', test_id=record.id)

    return render(request, 'test/index.html', context)

def test_result(request, test_id):
    test_result = BenchmarkTest.objects.get(pk=test_id)
    context = {
        'test_result': test_result
    }
    return render(request, 'test/result.html', context)


def program(request):
    return render(request, 'program/index.html')


def hard(request):
    profile = Profile.objects.get(user_id=request.user.id)
    profile.difficulty_mode = 1
    profile.save()

    workouts = WorkoutType.objects.filter(difficulty=1)
    context = {
        'workouts': workouts
    }
    return render(request, 'program/hard.html', context)


def extreme(request):
    profile = Profile.objects.get(user_id=request.user.id)
    profile.difficulty_mode = 2
    profile.save()

    workouts = WorkoutType.objects.filter(difficulty=2)
    context = {
        'workouts': workouts
    }
    return render(request, 'program/extreme.html', context)


def impossible(request):
    profile = Profile.objects.get(user_id=request.user.id)
    profile.difficulty_mode = 3
    profile.save()

    workouts = WorkoutType.objects.filter(difficulty=3)
    context = {
        'workouts': workouts
    }
    return render(request, 'program/impossible.html', context)


def leaderboard(request):
    users = User.objects.all()
    paginator = Paginator(users, 10)  # 2nd arg is num items per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'leaderboard.html', {'page_obj':page_obj})


@login_required
def workout(request):
    profile = Profile.objects.get(user_id=request.user.id)
    last_test = BenchmarkTest.objects.filter(user_id=request.user.id).order_by('id').last()
    last_workout = Workout.objects\
        .filter(user_id=request.user.id)\
        .order_by('id').last()
    if not last_workout:
        if not last_test:
            return redirect('pushups:test')
        workout_plan = WorkoutType.objects\
            .filter(difficulty=profile.difficulty_mode, day__exact=1, benchmark__lt=last_test.pushups)\
            .order_by('benchmark').last()
        return render(request, 'workout/index.html',
                      {'workout_plan': workout_plan, 'difficulty': profile.difficulty_mode})
    last_plan = WorkoutType.objects.get(id=last_workout.type.id)
    workout_plan = WorkoutType.objects\
        .filter(difficulty=profile.difficulty_mode, benchmark__gt=last_plan.benchmark)\
        .first()

    return render(request, 'workout/index.html',
                  {'workout_plan': workout_plan, 'difficulty': profile.difficulty_mode})


@login_required
def workout_form(request, workout_type_id):
    workout_plan = WorkoutType.objects.get(id=workout_type_id)
    form = WorkoutForm(request.POST or None)
    locked = False
    workouts_today = Workout.objects.filter(user=request.user, date=datetime.today())
    if workouts_today:
        locked = True

    if request.method == 'POST':
        if form.is_valid():
            set1 = form.cleaned_data.get('set1')
            set2 = form.cleaned_data.get('set3')
            set3 = form.cleaned_data.get('set3')
            set4 = form.cleaned_data.get('set4')
            set5 = form.cleaned_data.get('set5')
            total = set1 + set2 + set3 + set4 + set5
            sets = [
                set1,
                set2,
                set3,
                set4,
                set5
            ]
            if not request.user.is_authenticated:
                messages.warning(request, f'User not authenticated.')
                return redirect('pushups:workout')
            record = Workout(type=workout_plan, user=request.user, sets_completed=sets, total_pushups=total, date=timezone.now())
            record.save()
            profile = Profile.objects.get(user_id=request.user.id)
            profile.total_pushups = profile.total_pushups + total
            profile.save()
            return redirect('pushups:workout_result', record.id)

    return render(request, 'workout/form.html', {'workout_plan': workout_plan, 'form': form, 'locked':locked})


def workout_result(request, workout_id):
    username = request.user.username
    workout = Workout.objects.get(id=workout_id)
    pushups = 0
    for set in workout.sets_completed:
        pushups += set
    date = str(workout.date)
    return render(request, 'workout/result.html', {'pushups': pushups, 'date': date, 'username': username})
