class BigDataRouter:
    def db_for_read(self, model, **hints):
        if model._meta.label_lower == 'formapp.bigdata':
            return 'fdms'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.label_lower == 'formapp.bigdata':
            return 'fdms'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.label_lower == 'formapp.bigdata' or obj2._meta.label_lower == 'formapp.bigdata':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'formapp':
            return db == 'fdms'
        return None
