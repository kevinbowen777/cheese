import pytest
from factory.declarations import LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyChoice, FuzzyText
from django.template.defaultfilters import slugify

from cheese.users.tests.factories import UserFactory

from ..models import Cheese


@pytest.fixture
def cheese():
    return CheeseFactory()


class CheeseFactory(DjangoModelFactory):
    name = FuzzyText()
    slug = LazyAttribute(lambda obj: slugify(obj.name))
    description = Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    firmness = FuzzyChoice([x[0] for x in Cheese.Firmness.choices])
    country_of_origin = Faker("country_code")
    creator = SubFactory(UserFactory)

    class Meta:
        model = Cheese
        skip_postgeneration_save = True
