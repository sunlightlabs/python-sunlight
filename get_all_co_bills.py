#!/usr/bin/env python

import sunlight

os = sunlight.OpenStates()
print os.bills(state="co")

cw = sunlight.CapitolWords()
print cw.text(phrase="united states")
