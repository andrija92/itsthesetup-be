import factory
from factory.django import DjangoModelFactory
from api.models import SetupData, User, Test, Setup

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    testerino_fielderino = factory.Faker('boolean')
    sto_ti_cinis = factory.Faker('text')


class SetupDataFactory(DjangoModelFactory):
    class Meta:
        model = SetupData

    data = factory.Faker('json')
    notes = factory.Faker('text')

class SetupFactory(DjangoModelFactory):
    class Meta:
        model = Setup

    user = factory.SubFactory(UserFactory)
    created_at = factory.Faker('date_time')
    title = factory.Faker('sentence')
    gameId = factory.Faker('uuid4')
    car = factory.Faker('sentence')
    track = factory.Faker('sentence')
    description = factory.Faker('text')
    setupData = factory.SubFactory(SetupDataFactory)
    videoUrl = factory.Faker('url')
    rating = factory.Faker('random_int')
    ratingCount = factory.Faker('random_int')
    downloads = factory.Faker('random_int')