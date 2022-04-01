import ast

from csv import DictReader

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

from enoki_app.models import CustomUser

base_dir = settings.BASE_DIR

class Command(BaseCommand):
    help = '''
        Create users stored in csv file.
        Once users are created, it is mandatory for them to modify their password at their first connection to the service.
    '''

    def handle(self, *args, **options):
        with open(
            file = base_dir / 'media/csv/users.csv',
            mode = 'r',
            encoding = 'UTF8',
            newline = ''
        ) as csv_file:

            users_dict = DictReader(csv_file, delimiter = ',')
            for user in users_dict:
                #ast library allows us to parse the type of a value. In this case, it turns "False" and "True" value stored in string in csv file for is_superuser column into boolean value. Thus, we are able to test whether or not the user is a superuser.
                if ast.literal_eval(user['is_superuser']):
                    CustomUser.objects.create_superuser(
                        nickname = user['nickname'],
                        email = user['email'],
                        password = user['password']
                    )
                else:
                    CustomUser.objects.create_user(
                        nickname = user['nickname'],
                        email = user['email'],
                        password = user['password']
                    )

        self.stdout.write(self.style.SUCCESS('Users successfully created'))