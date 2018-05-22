import django_tables2 as tables
from core import models


class ANiceTable(tables.Table):
    class Meta:
        model = models.ANiceModel
