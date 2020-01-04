$(function() {

	function FilamentBoxHealthCheckViewModel(parameters) {
		var self=this;
		self.loginState = parameters[0];

		self.onDataUpdaterPluginMessage = function(plugin, data) {
			if(plugin != "FilamentBoxHealthCheck") {
				alert(plugin);
				return;
			}
			else {
				alert("yay: !" + data.temperature)
				alert($("bme280-temp").text + ", " +$("filmanetBoxHealthCheck").text);
			}
		}
	}
	OCTOPRINT_VIEWMODELS.push([
		constuct: FilamentBoxHealthCheckViewModel,
		dependencies: [],
		elements: ["#FilamentBoxHealthCheck"]
	]);
});
