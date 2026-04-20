import datetime

import factory
from faker import Faker
from factory.django import DjangoModelFactory

from api.models import Setup, SetupData, User, Game, Car, Track

_fake = Faker()


def _fake_car_name() -> str:
    return " ".join(_fake.words(nb=3, unique=False)).title()[:255]


def _fake_track_name() -> str:
    return f"{_fake.city()} — {_fake.word().title()}"[:255]


def _fake_setup_data_dict() -> dict:
    return {
        "springs": _fake.pyint(min_value=1, max_value=10),
        "arb": _fake.pyfloat(min_value=0.5, max_value=8, right_digits=1),
        "wings": {
            "front": _fake.pyint(min_value=0, max_value=8),
            "rear": _fake.pyint(min_value=0, max_value=12),
        },
        "damper": _fake.pyint(min_value=1, max_value=30),
    }


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    testerino_fielderino = factory.Faker("pybool")
    sto_ti_cinis = factory.Faker("text", max_nb_chars=500)

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        raw = extracted if extracted is not None else _fake.password(
            length=14,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
        self.set_password(raw)
        if create:
            self.save(update_fields=["password"])


class TrackFactory(DjangoModelFactory):
    class Meta:
        model = Track

    name = factory.Faker("city")
    location = factory.Faker("country")
    description = factory.Faker("text", max_nb_chars=2000)

    @factory.post_generation
    def games(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.games.add(*extracted)


class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car

    description = factory.Faker("text", max_nb_chars=2000)
    brand = factory.Faker("company")
    model = factory.Faker("word")

    @factory.post_generation
    def games(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.games.add(*extracted)


class SetupDataFactory(DjangoModelFactory):
    class Meta:
        model = SetupData

    data = factory.LazyFunction(_fake_setup_data_dict)
    notes = factory.Faker("text", max_nb_chars=1000)


class SetupFactory(DjangoModelFactory):
    user = factory.Iterator(User.objects.all())
    game = factory.Iterator(Game.objects.all())
    car = factory.Iterator(Car.objects.all())
    track = factory.Iterator(Track.objects.all())

    class Meta:
        model = Setup

    created_at = factory.Faker(
        "date_time_between",
        start_date="-2y",
        end_date="now",
        tzinfo=datetime.timezone.utc,
    )

    title = factory.Faker("catch_phrase")
    description = factory.Faker("text", max_nb_chars=2000)
    setupData = factory.SubFactory(SetupDataFactory)
    videoUrl = "https://www.youtube.com/watch?v=ucA-amwAEKU"
    rating = factory.Faker("pyint", min_value=0, max_value=5)
    ratingCount = factory.Faker("pyint", min_value=0, max_value=5000)
    downloads = factory.Faker("pyint", min_value=0, max_value=50_000)
