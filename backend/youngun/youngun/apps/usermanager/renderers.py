from youngun.apps.core.renderers import YoungunJSONRenderer


class BrandJSONRenderer(YoungunJSONRenderer):
    object_label = 'brand'
    object_label_plural = 'brands'


class ProfileJSONRenderer(YoungunJSONRenderer):
    object_label = 'profile'
    object_label_plural = 'profiles'
