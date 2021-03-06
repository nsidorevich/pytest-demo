import logging.config
import os
import yaml

from zebrunnerpy import connector_obj, PyTestZafiraListener

pytest_plugins = ['zebrunnerpy.plugin']
is_zafira_plugged_in = True
connector_obj.pytest_listener = PyTestZafiraListener(connector_obj.state)


def apply_initial_logging_configuration():
    path = os.getcwd()
    config = yaml.load(open(os.path.join(path, 'logging.cfg'), 'r'))
    logging.config.dictConfig(config)


def pytest_configure(config):
    """
    Attaches wrapped hooks as plugin
    """
    config.pluginmanager.register(connector_obj.pytest_listener)
    apply_initial_logging_configuration()
