from django.apps import AppConfig


class CampaignAppConfig(AppConfig):
    name = 'youngun.apps.campaigns'
    label = 'campaigns'
    verbose_name = 'Campaigns'

    def ready(self):
        import youngun.apps.campaigns.signals


default_app_config = 'youngun.apps.campaigns.CampaignAppConfig'
