import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from AppTwo.models import User
from faker import Faker 

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.free_email()

        userobj = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(10)
    print("populating complete")