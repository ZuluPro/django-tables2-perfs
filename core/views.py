from django_tables2 import SingleTableView
from core import models
from core import tables


class WithTablePaginationList(SingleTableView):
    model = models.ANiceModel
    table_class = tables.ANiceTable
    table_pagination = {
        'per_page': 1000,
    }


class WithDjangoPaginationList(SingleTableView):
    model = models.ANiceModel
    table_class = tables.ANiceTable
    paginated_by = 1000
