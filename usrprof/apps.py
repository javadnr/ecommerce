from django.apps import AppConfig


class UsrprofConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usrprof'

    def ready(self):
        import usrprof.signals
        