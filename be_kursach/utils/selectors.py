from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class SelectorBaseByMethodModelSerializer(ModelSerializer):
    text = SerializerMethodField()
    value = SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self.Meta.fields = ('value', 'text')
        super().__init__(*args, **kwargs)

    def get_value(self, object):
        return getattr(object, self.context['view'].lookup_field, 'pk')

    def get_text(self, object):
        return object.__str__()
