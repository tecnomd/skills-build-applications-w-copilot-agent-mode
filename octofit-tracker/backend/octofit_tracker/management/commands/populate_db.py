from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Daten löschen
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        Team.objects.create(name='marvel', description='Marvel Superheroes')
        Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True)
        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True)
        User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True)
        User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True)

        # Activities
        Activity.objects.create(user_email='ironman@marvel.com', type='run', duration=30, date='2025-10-17')
        Activity.objects.create(user_email='spiderman@marvel.com', type='swim', duration=45, date='2025-10-16')
        Activity.objects.create(user_email='batman@dc.com', type='cycle', duration=60, date='2025-10-15')
        Activity.objects.create(user_email='wonderwoman@dc.com', type='yoga', duration=50, date='2025-10-14')

        # Leaderboard
        Leaderboard.objects.create(team_name='marvel', points=150)
        Leaderboard.objects.create(team_name='dc', points=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Squats', description='Do 30 squats', suggested_for='dc')

        print('Testdaten erfolgreich eingefügt!')
