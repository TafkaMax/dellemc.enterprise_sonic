#
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the sonic facts module.
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class FactsArgs(object):  # pylint: disable=R0903

    """ The arg spec for the sonic facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        'vlans',
        'snmp',
        'interfaces',
        'lag_interfaces',
        'l3_interfaces',
        'bgp',
        'l2_interfaces',
        'vrf_interfaces',
        'vxlans'
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list'),
        'gather_network_resources': dict(choices=choices,
                                         type='list'),
    }