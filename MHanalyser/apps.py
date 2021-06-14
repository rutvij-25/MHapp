from django.apps import AppConfig


class MhanalyserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MHanalyser'

    def ready(self):
        import MHanalyser.signals
