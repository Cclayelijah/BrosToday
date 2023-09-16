from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from pushups.models import Workout, BenchmarkTest


def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            user = User.objects.get(username=username)
            profile = Profile(user=user)
            profile.save()

            messages.success(request, f'Welcome {username}!')
            return redirect("login")
        else:
            form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profilepage(request):
    total_workouts = Workout.objects.filter(user_id=request.user.id).count()
    benchmark = request.user.profile.get_benchmark()
    rank = request.user.profile.get_rank()

    return render(request, 'users/profile.html',
                  {'total_workouts': total_workouts, 'benchmark': benchmark, 'rank': rank})