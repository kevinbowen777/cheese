import pytest

from .factories import CheeseFactory
from ..models import Cheese  # noqa:F401


# Connects our tests with our database
pytestmark = pytest.mark.django_db


def test__str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name


def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f"/cheeses/{cheese.slug}/"
