# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import time
import bme280
import smbus2
import sys

from octoprint.util import RepeatedTimer

class FilamentBoxHealth(octoprint.plugin.StartupPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.AssetPlugin):
 
    def on_after_startup(self):
        self._logger.info("started Filament Box Healthcheck Plugin: ")
        t = RepeatedTimer(15, self.check_resources, run_first=True)
        t.start()

    def check_resources(self):
        self._logger.warning("now I'm running ..")
        message = pull_bme280()
        self._logger.warning("now I'm dead. This log info does not appear.")
        self.plugin_manager.send_plugin_message("FilamentBoxHealthCheck", message)

    def get_assets(self):
        return dict(
                js=["js/FilamentBoxHealthCheck.js"]
        )

    def pull_bme280(self, bus=1, address=0x76):
        bus = smbus2.SMBus(bus)

        #as soon as the bme lib is used, everything breaks down. works fine on console with source set to oprint/bin/activate
        try:
            calibration_params=bme280.load_calibration_params(bus, address)
            data = bme280.sample(bus, address, bme280.load_calibration_params(bus, address))
        except:
            e = sys.exc_info()[0]
            print(e)

        message = dict(
                humidity=data.humidity,
                temperature=data.temperature,
                pressure=data.pressure 
                )
        return message


if __name__ == "__main__":
    print("running ...")
    print(FilamentBoxHealth().pull_bme280())


__plugin_pythoncompat__ =">2.7,<4"
__plugin_name__ = "Filament Box Health Check"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Temperature & humidity from the Pi via the I2C interface"
__plugin_implementation__ = FilamentBoxHealth()

