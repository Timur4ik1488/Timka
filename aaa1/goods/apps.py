from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    # поменяли название "главы"  в панели админов
    verbose_name = 'Товары'
