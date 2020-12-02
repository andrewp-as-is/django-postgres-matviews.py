from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('matview', nargs='+', type=str)

    def handle(self, *args, **options):
        cursor = connection.cursor()
        for matview in options['matview']:
            sql = """REFRESH MATERIALIZED VIEW "%s";""" % matview
            cursor.execute(sql)
