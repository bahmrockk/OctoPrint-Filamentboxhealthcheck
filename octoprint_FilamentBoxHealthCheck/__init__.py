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
        t = RepeatedTimer(60, self.check_resources, run_first=True)
        t.start()

    def check_resources(self):
        message = self.pull_bme280() #thanks @ tedder42 for helping me move forward!
        self._plugin_manager.send_plugin_message(self._identifier, message)

    def get_assets(self):
        return dict(
                js=["js/FilamentBoxHealthCheck.js"]
        )

    def pull_bme280(self, bus=1, address=0x76):
        bus = smbus2.SMBus(bus)
        try:
            calibration_params=bme280.load_calibration_params(bus, address)
            data = bme280.sample(bus, address, bme280.load_calibration_params(bus, address))
        except:
            e = sys.exc_info()[0]
            self_logger.error("%s", e)

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
__plugin_implementation__ = FilamentBoxHealth()

