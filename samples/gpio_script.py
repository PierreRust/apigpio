import asyncio
import apigpio

LED_GPIO = 21


@asyncio.coroutine
def start(pi, address, gpio):
    yield from pi.connect(address)

    yield from pi.set_mode(gpio, apigpio.OUTPUT)

    # Create the script.
    script = 'w {e} 1 mils 500 w {e} 0 mils 500 w {e} 1 mils 500 w {e} 0'\
        .format(e=gpio)
    sc_id = yield from pi.store_script(script)

    # Run the script.
    yield from pi.run_script(sc_id)

    yield from asyncio.sleep(5)

    yield from pi.delete_script(sc_id)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    pi = apigpio.Pi(loop)
    address = ('192.168.1.3', 8888)
    loop.run_until_complete(start(pi, address, LED_GPIO))
