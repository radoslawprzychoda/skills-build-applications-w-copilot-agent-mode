from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Superhero team')
        self.assertEqual(team.name, 'Marvel')
        self.assertEqual(team.description, 'Superhero team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test User', email='test2@example.com', team='DC')
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-21')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(str(activity.date), '2025-12-21')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(name='Test User', email='test3@example.com', team='Marvel')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', description='Upper body', difficulty='Easy')
        self.assertEqual(workout.name, 'Push Ups')
        self.assertEqual(workout.description, 'Upper body')
        self.assertEqual(workout.difficulty, 'Easy')
