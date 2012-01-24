#!/usr/bin/env python

from sunlight import OpenStates
import sunlight.service

os = OpenStates()
print os.get('bills', state="co")
