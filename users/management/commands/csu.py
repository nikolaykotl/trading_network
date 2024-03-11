import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email= 'nikkot198@gmail.com', #os.getenv('EMAIL'),
            first_name= 'Admin', #os.getenv('FIRST_NAME'),
            last_name= 'Nikkot', #os.getenv('LAST_NAME'),
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe') #os.getenv('PASSWORD'))
        user.save()
