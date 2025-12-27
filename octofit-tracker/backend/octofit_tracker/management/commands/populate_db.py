from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
            steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
            bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
            clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=tony, type='Running', duration=30, date='2025-12-01')
            Activity.objects.create(user=steve, type='Cycling', duration=45, date='2025-12-02')
            Activity.objects.create(user=bruce, type='Swimming', duration=60, date='2025-12-03')
            Activity.objects.create(user=clark, type='Yoga', duration=20, date='2025-12-04')

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(user=tony, score=120)
            Leaderboard.objects.create(user=steve, score=110)
            Leaderboard.objects.create(user=bruce, score=130)
            Leaderboard.objects.create(user=clark, score=125)

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            Workout.objects.create(name='Push Ups', description='Upper body strength', difficulty='Easy')
            Workout.objects.create(name='Pull Ups', description='Back and arms', difficulty='Medium')
            Workout.objects.create(name='Squats', description='Legs and glutes', difficulty='Easy')
            Workout.objects.create(name='Plank', description='Core strength', difficulty='Hard')

            self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
