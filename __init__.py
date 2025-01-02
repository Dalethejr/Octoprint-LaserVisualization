import octoprint.plugin

class LaserVisualizationPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]
__plugin_name__ = "Laser Visualization"
__plugin_version__ = "0.0.1"
__plugin_description__ = "A quick \"Hello World\" example plugin for OctoPrint"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = LaserVisualizationPlugin()