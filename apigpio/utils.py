
class Debounce(object):
    """
    Simple debouncing decorator for apigpio callbacks.

    Example:

    `@Debouncer()
     def my_cb(gpio, level, tick)
         print('gpio cb: {} {} {}'.format(gpio, level, tick))
    `

    The threshold can be given to the decorator as an argument (in millisec).
    """

    def __init__(self, threshold=100):
        self.last = 0
        self.threshold = threshold/1000

    def __call__(self, pigpio_cb):
        def _wrapped_cb(*args, **kwargs):
            tick = args[2]
            if tick - self.last > self.threshold:
                pigpio_cb(*args, **kwargs)
                self.last = tick
        return _wrapped_cb
