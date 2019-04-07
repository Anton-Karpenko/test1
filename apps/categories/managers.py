from django.db.models import QuerySet, Count


class CategoryQuerySet(QuerySet):
    def with_counts(self):
        return self \
            .annotate(subcategories_count=Count('subcategories', distinct=True)) \
            .annotate(items_count=Count('items', distinct=True))
