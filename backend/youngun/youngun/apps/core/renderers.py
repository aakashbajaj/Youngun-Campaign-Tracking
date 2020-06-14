import json

from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList


class YoungunJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    object_label_plural = 'objects'
    # pagination_object_label = 'objects'
    # pagination_object_count = 'count'

    def render(self, data, media_type=None, renderer_context=None):
        # if data.get('results', None) is not None:
        #     return json.dumps({
        #         self.pagination_object_label: data['results'],
        #         self.pagination_count_label: data['count']
        #     })

        if isinstance(data, ReturnList):
            _data = json.loads(
                super(YoungunJSONRenderer, self).render(data).decode('utf-8'))

            return json.dumps({self.object_label_plural: _data})

        elif data.get('errors', None) is not None:
            return super(YoungunJSONRenderer, self).render(data)

        else:
            return json.dumps({
                self.object_label: data
            })
