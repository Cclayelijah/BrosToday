from django.db import models
from django.contrib.auth.models import User
from pushups.models import Workout, BenchmarkTest


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.jpeg', upload_to='profile_pictures')
    location = models.CharField(max_length=100, default='Earth')
    difficulty_mode = models.IntegerField(default=1)
    total_pushups = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

    def get_benchmark(self):
        last_workout = Workout.objects.filter(user_id=self.user.id).order_by('id').last()
        last_test = BenchmarkTest.objects.filter(user_id=self.user.id).order_by('id').last()
        benchmark = 0
        if last_test:
            benchmark = last_test.pushups
        if last_workout:
            benchmark = 0
            for set in last_workout.sets_completed:
                benchmark += set
        return benchmark

    def get_rank(self):
        users = Profile.objects.all().order_by('-total_pushups')
        rank = 1
        for user in users:
            if self.id == user.id:
                return rank
            rank += 1
        return "Not Found"
