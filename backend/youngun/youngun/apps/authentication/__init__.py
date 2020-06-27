from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'youngun.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import youngun.apps.authentication.signals


default_app_config = "youngun.apps.authentication.AuthenticationAppConfig"
