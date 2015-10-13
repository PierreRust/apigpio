# apigpio
apigpio - an asyncio-based python client for pigpio


The [pigpio](http://abyz.co.uk/rpi/pigpio/pigpiod.html) provides a very convenient `pigpiod` daemon whcih can be used through a pipe or socket interface to access GPIOs on the Raspberry Pi. 

`apigpio` is a python client library that uses asyncio to access the `pigpiod` daemon. It's basically a port of the original python client provided with pigpio.

