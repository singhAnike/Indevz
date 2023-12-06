import random
import string
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Create dummy data for testing'

    def handle(self, *args, **options):
        User = get_user_model()

        # Create dummy users
        for _ in range(10):
            username = fake.user_name()
            email = fake.email()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            phone = fake.phone_number()
            company_name = fake.company()
            access_code = ''.join(random.choices(string.digits, k=4))

            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone=phone,
                company_name=company_name,
                access_code=access_code
            )

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully'))
