apigpio
=======

apigpio - an asyncio-based python client for pigpio


`pigpio <http://abyz.co.uk/rpi/pigpio/pigpiod.html>`_ provides a very 
convenient `pigpiod` daemon which can be used through a pipe or socket interface
to access GPIOs on the Raspberry Pi. 

`apigpio` is a python client library that uses asyncio to access the `pigpiod` 
daemon. It's basically a (incomplete) port of the original python client provided with pigpio.

Installation
============

apigpio is available on Pypi and can be installed with pip::

  pip install apigpio

To install it from sources: :
 
  git clone https://github.com/PierreRust/apigpio.git
  cd apigpio
  python setup.py install
    
    
Usage
=====

See the examples in the `samples` directory.
