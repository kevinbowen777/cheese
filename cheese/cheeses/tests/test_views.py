import pytest
from pytest_django.asserts import (
    assertContains,
    assertRedirects,
)

from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

from cheese.users.models import User
from ..models import Cheese
from ..views import (
    CheeseCreateView,
    CheeseListView,
    CheeseDetailView,
)
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


def test_good_cheese_list_view_expanded(rf):
    # Determine the URL
    # url = reverse("cheeses:list")
    # rf is the pytest shortcut to django.test.RequestFactory
    # we generate a request as if from a user accessing
    #   the cheese list view
    # request = rf.get(url)
    request = rf.get(reverse("cheeses:list"))
    # Call as_view() to make a callable object
    # callable_obj is analogous to a function-based view
    # callable_obj = CheeseListView.as_view()
    # Pass in the request into the callable_obj to get an
    #   HTTP response served up by Django
    # response = callable_obj(request)
    response = CheeseListView.as_view()(request)
    # Test that the HTTP response has 'Cheese List' in the
    #   HTML and has a 200 response code
    assertContains(response, 'Cheese List')

def test_good_cheese_detail_view(rf):
    # Order some cheese from the CheeseFactory
    cheese = CheeseFactory()
    # Make a request for our new cheese
    url = reverse("cheeses:detail", kwargs={"slug": cheese.slug})
    request = rf.get(url)

    # Use the request to get the response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    # Test that the response is valid
    assertContains(response, cheese.name)
