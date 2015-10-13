import asyncio
import apigpio

BT1_GPIO = 18
BT2_GPIO = 23


def on_input(gpio, level, tick):
    print('on_input {} {} {}'.format(gpio, level, tick))


@asyncio.coroutine
def subscribe(pi):

    yield from pi.set_mode(BT1_GPIO, apigpio.INPUT)
    yield from pi.set_mode(BT2_GPIO, apigpio.INPUT)

    yield from pi.add_callback(BT1_GPIO, edge=apigpio.RISING_EDGE,
                               func=on_input)
    yield from pi.add_callback(BT2_GPIO, edge=apigpio.RISING_EDGE,
                               func=on_input)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    pi = apigpio.Pi(loop)
    address = ('192.168.1.3', 8888)
    loop.run_until_complete(pi.connect(address))
    loop.run_until_complete(subscribe(pi))

    loop.run_forever()
