from haystack import indexes

from example.apps.things.models import Thing


class ThingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(indexed=False, model_attr='name')
    url = indexes.CharField(indexed=False, model_attr='get_absolute_url')

    def get_model(self):
        return Thing

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
