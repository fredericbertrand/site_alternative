from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('first')
        parser.add_argument('--option1')

    def handle(self, *args, **options):
        print("this is my first command with Django !")
        print(f'#1 door: {options["first"]}')