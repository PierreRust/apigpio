import functools


def Debounce(threshold=100):
    """
    Simple debouncing decorator for apigpio callbacks.

    Example:

    `@Debouncer()
     def my_cb(gpio, level, tick)
         print('gpio cb: {} {} {}'.format(gpio, level, tick))
    `

    The threshold can be given to the decorator as an argument (in millisec).
    This decorator can be used both on function and object's methods.
    """
    threshold = threshold/100

    class _decorated(object):

        def __init__(self, pigpio_cb):
            self._fn = pigpio_cb
            self.last = 0
            self.is_method = False

        def __call__(self, *args, **kwargs):
            if self.is_method:
                tick = args[3]
            else:
                tick = args[2]
            if tick - self.last > threshold:
                self._fn(*args, **kwargs)
                self.last = tick

        def __get__(self, instance, type=None):
            # with is called when an of `_decorated` is used as a class
            # attribute, which is the case when decorating a method in a class
            self.is_method = True
            return functools.partial(self, instance)

    return _decorated
