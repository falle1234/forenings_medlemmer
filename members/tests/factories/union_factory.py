import factory
from factory import Faker, DjangoModelFactory, SubFactory
from factory.fuzzy import FuzzyChoice

from members.models import Union
from members.tests.factories import AddressFactory
from members.tests.factories.factory_helpers import TIMEZONE


class UnionFactory(DjangoModelFactory):
    class Meta:
        model = Union

    name = factory.LazyAttribute(lambda u: "Coding Pirates {}".format(u.address.city))
    chairman_old = Faker("name")
    chairman_email_old = Faker("email")
    second_chair_old = Faker("name")
    second_chair_email_old = Faker("email")
    cashier_old = Faker("name")
    cashier_email_old = Faker("email")
    secretary_old = Faker("name")
    secretary_email_old = Faker("email")
    union_email = Faker("email")
    statues = Faker("url")
    founded = Faker("date_time", tzinfo=TIMEZONE)
    region = FuzzyChoice([r[0] for r in Union.regions])
    address = SubFactory(AddressFactory)
    board_members_old = Faker("text")
    bank_main_org = Faker("boolean")
    bank_account = Faker("numerify", text="####-##########")
