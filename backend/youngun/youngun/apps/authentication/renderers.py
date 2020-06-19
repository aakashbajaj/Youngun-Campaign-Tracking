from youngun.apps.core.renderers import YoungunJSONRenderer


class UserInfoJSONRenderer(YoungunJSONRenderer):
    object_label = 'user'
    object_label_plural = 'users'


class OrganisationJSONRenderer(YoungunJSONRenderer):
    object_label = 'organisation'
    object_label_plural = 'organisations'
