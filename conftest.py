from zebrunnerpy import connector_obj, PyTestZafiraListener

pytest_plugins = ['zebrunnerpy.plugin']
is_zafira_plugged_in = True
connector_obj.pytest_listener = PyTestZafiraListener(connector_obj.state)


def pytest_configure(config):
    """
    Attaches wrapped hooks as plugin
    """
    config.pluginmanager.register(connector_obj.pytest_listener)
