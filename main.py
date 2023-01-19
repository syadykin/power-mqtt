import time

# sleep delay is necessary for correct init
time.sleep(5)

from machine import Pin

from mqtt_async import MQTTClient, config
import uasyncio as asyncio

from must import Must
from pylontech import Pylontech

from settings import *

config['server'] = MQTT_HOST
config['ssid'] = WIFI_SSID
config['wifi_pw'] = WIFI_PASSWORD

pylontech = Pylontech(
    uart_id=PYLONTECH_UART,
    pins=[Pin(PYLONTECH_TX), Pin(PYLONTECH_RX)])
must = Must(
    uart_id=MUST_UART,
    pins=[Pin(MUST_TX), Pin(MUST_RX)],
    ctrl_pin=MUST_CTRL)

async def print_mqtt(client, prefix, value):
    for key in value.keys():
        val = str(value[key])
        name = '{}/{}'.format(prefix, key)

        await client.publish(name, val)

async def read_must(client):
    while True:
        try:
            values = must.get_values(MUST_ADDR)
            await print_mqtt(client, MUST_PREFIX, values)
        except OSError:
            pass

        await asyncio.sleep(MUST_INTERVAL)

async def read_pylontech(client):
    while True:
        for x in range(2, 2 + PYLONTECH_BATT):
            try:
                values = pylontech.get_values(x)
                await print_mqtt(
                    client,
                    '{}/{}'.format(PYLONTECH_PREFIX, x),
                    values)
            except ValueError:
                pass
            except AssertionError:
                pass

        await asyncio.sleep(PYLONTECH_INTERVAL)


async def main(client):
    await client.connect()

    for coroutine in (read_must, read_pylontech):
        asyncio.create_task(coroutine(client))

    while True:
        await asyncio.sleep(600)

client = MQTTClient(config)
while True:
    try:
        asyncio.run(main(client))
    except OSError:
        print("Can't connect")



