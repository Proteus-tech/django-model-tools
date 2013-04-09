from functools import wraps
from django.db import IntegrityError

def force_save_not_null_nor_blank(*attribute_name_iter):
    """
    Decorator to be used with the "save" function of a model class to force certain fields to not be blank.
    Would also throw error if the field doesn't exist or the field is null

    usage:

    @force_save_not_null_nor_blank('a_field', 'b_field', 'c_field')
    def save(self, force_insert=False, force_update=False, using=None):
        super(ClassName, self).save(force_insert, force_update, using)
    """
    def wrapper(func):
        def check_not_null_nor_blank(instance, *args,**kwargs):
            if attribute_name_iter:
                for attribute_name in attribute_name_iter:
                    attr = getattr(instance, attribute_name)
                    if not attr or (isinstance(attr, basestring) and len(attr.strip()) == 0):
                        raise IntegrityError('%s.%s may not be NULL or BLANK' % (instance.__class__.__name__, attribute_name))
                return func(instance, *args, **kwargs)
        return wraps(func)(check_not_null_nor_blank)
    return wrapper