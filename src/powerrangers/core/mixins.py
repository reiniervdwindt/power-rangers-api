class MultiSerializerViewSetMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        try:
            return self.serializer_classes[self.action]
        except (KeyError, AttributeError):  # pragma: no cover
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()
