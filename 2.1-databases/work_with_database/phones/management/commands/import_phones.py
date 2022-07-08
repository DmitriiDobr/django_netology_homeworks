import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-i',
            '--import',
            action='store_true',
            default=True,
            help='Вывод короткого сообщения'
        )

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(id=phone['id'],
                                 name=phone['name'],
                                 price=phone["price"],
                                 image=phone["image"],
                                 release_date=phone["release_date"],
                                 lte_exists=phone["lte_exists"],
                                 slug=slugify(phone['name']))
