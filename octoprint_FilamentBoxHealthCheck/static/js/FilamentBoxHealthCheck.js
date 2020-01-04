$(function() {

	function FilamentBoxHealthCheckViewModel(parameters) {
		var self=this;
		
		self.bme280Humidity = ko.observable();
		self.bme280Temperature = ko.observable();

		self.onDataUpdaterPluginMessage = function(plugin, data) {
			if(plugin != "FilamentBoxHealthCheck") {
				return;
			}
			else {
				
				self.bme280Temperature(Math.round(data.temperature*100)/100);
				self.bme280Humidity(Math.round(data.humidity*100)/100);
			}
		}
	}
	OCTOPRINT_VIEWMODELS.push([
		FilamentBoxHealthCheckViewModel,
		[],
		["#navbar_plugin_FilamentBoxHealthCheck"]
	]);
});
