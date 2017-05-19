# -*- coding: utf-8 -*-

import yaml

'''
I really despise software that keeps its configuration in the syntax of the language in which the software is written - I’m looking at you, Drupal. Users should not need to know PHP, Python, or Ruby in order to customize settings. That’s why storing settings as YAML is vastly superior since it’s easy for humans to parse at a casual glance. So, what’s the best and most Pythonic way to provide settings globally across a project?
'''
with open("config/settings.yaml", "r") as f:
    settings = yaml.load(f)

