from youngun.apps.core.renderers import YoungunJSONRenderer


class UserInfoJSONRenderer(YoungunJSONRenderer):
    object_label = 'user'
    object_label_plural = 'users'
