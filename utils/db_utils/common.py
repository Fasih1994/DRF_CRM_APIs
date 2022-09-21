from logging.config import dictConfig
from drf_apis.log_config import LOG_SETTINGS
import functools
from utils.db_utils.db_connection import get_oracle_db

dictConfig(LOG_SETTINGS)


def get_curr_time_unix():
    import time
    return int(time.time())


def get_curr_datetime():
    import datetime
    return datetime.datetime.now()


def set_sql_for_field(field, sql):
    """
    Decorator for Model.save() to set SQL for field if empty.

    Example:

    class LegacyModel(models.Model):
        col1 = models.IntegerField(primary_key=True)
        col2 = models.IntegerField()

        @set_sql_for_field('col1', 'select col1_seq.nextval from dual')
        @set_sql_for_field('col2', 'select 1+max(col2) from legacy_model')
        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

    When this model is saved col1 and col2 will be set (if empty) to the output
    of the provided SQL within the schema/database of the model's app.
    """
    def decorator(model_save_func):
        @functools.wraps(model_save_func)
        def wrapper(obj, *args, **kwargs):
            assert hasattr(obj, field), (
                'set_sql_for_field was given a field that does not exist on '
                'the model. Double-check model fields and decorators for '
                f'{obj.__class__}.{field} and SQL {sql}'
            )

            if getattr(obj, field) is None:
                # Multi-DB safe! Get DB for class from default manager.
                database = obj.__class__._default_manager.db

                conn = get_oracle_db()
                cursor = conn.cursor()
                cursor.execute(f'{sql}')
                setattr(obj, field, cursor.fetchone()[0])
                cursor.close()
                conn.close()

            return model_save_func(obj, *args, **kwargs)
        return wrapper
    return decorator


