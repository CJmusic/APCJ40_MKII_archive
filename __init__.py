#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/APCJ40_MkII/__init__.py
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, SYNC, REMOTE, controller_id, inport, outport
from .APCJ40_MkII import APCJ40_MkII

def create_instance(c_instance):
    return APCJ40_MkII(c_instance)


def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[41], model_name=u'Akai APC40 MkII'),
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SYNC, SCRIPT, REMOTE])]}
