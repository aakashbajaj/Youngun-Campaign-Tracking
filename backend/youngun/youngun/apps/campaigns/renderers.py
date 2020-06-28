from youngun.apps.core.renderers import YoungunJSONRenderer


class LiveCampaignMetricJSONRenderer(YoungunJSONRenderer):
    object_label = 'campaign'
    object_label_plural = 'campaigns'


class CampaignDataJSONRenderer(YoungunJSONRenderer):
    object_label = 'campaign'
    object_label_plural = 'campaigns'
