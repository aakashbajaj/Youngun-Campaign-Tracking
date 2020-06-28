from django.apps import AppConfig


class ContentAppConfig(AppConfig):
    name = 'youngun.apps.content'
    label = 'content'
    verbose_name = 'Content'

    def ready(self):
        import youngun.apps.content.signals


default_app_config = 'youngun.apps.content.ContentAppConfig'
