from datetime import datetime

import factory
from django.utils import timezone
from faker import Faker

from bhealthapp.models import Country, City, User, Lab, UserRating, Type, Service, LabService, Appointment, Result, \
    Notification

fake = Faker()


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = fake.name()


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = fake.name()
    country = CountryFactory()
    postal_code = "20103104adad9##"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.username()
    profile_picture = 'fake.jpg'
    profile_link = "http://profilelink.com"
    password = fake.password()
    phone_number = "0303030330"
    email = fake.email()
    dob = factory.Faker("date_time", tzinfo=timezone.utc)
    address = fake.text()
    city = CityFactory
    is_blocked = False
    is_email_verified = False
    gender = 0


class LabFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lab

    city = CityFactory
    name = fake.name()
    password = fake.password()
    address = fake.text()
    phone_number = "0303030330"
    email = fake.email()
    website = "http://websitelink.com"


class UserRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserRating

    user = UserFactory
    lab = LabFactory
    rating = 0


class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Type

    name = fake.name()
    description = fake.text()


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Service


name = fake.name()
duration = datetime.timedelta(days=-1, seconds=68400),
type = TypeFactory


class LabServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LabService

    lab_service = LabFactory
    service = ServiceFactory


class AppointmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Appointment

    lab_appointment = LabFactory
    service_appointment = ServiceFactory
    patient = UserFactory
    date = factory.Faker("date_time", tzinfo=timezone.utc)
    status = 0


class ResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Result

    appointment = AppointmentFactory
    pdf = "Result.pdf"


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    notification_appointment = AppointmentFactory
    message = "Notification!"
    is_confirmed = False
    is_declined = False
