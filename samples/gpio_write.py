import asyncio
import apigpio

LED_GPIO = 21


@asyncio.coroutine
def start_blink(pi, address):
    yield from pi.connect(address)

    yield from pi.set_mode(LED_GPIO, apigpio.OUTPUT)

    while True:
        yield from pi.write(LED_GPIO, 0)
        yield from asyncio.sleep(1)
        yield from pi.write(LED_GPIO, 1)
        yield from asyncio.sleep(1)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    pi = apigpio.Pi(loop)
    address = ('192.168.1.3', 8888)
    loop.run_until_complete(start_blink(pi, address))
