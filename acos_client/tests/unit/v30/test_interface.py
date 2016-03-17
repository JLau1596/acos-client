# Copyright (C) 2016, A10 Networks Inc. All rights reserved.

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock
import unittest2 as unittest

from acos_client.v30 import interface


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.client = mock.MagicMock()
        self.target = interface.Interface(self.client)
        self.url_prefix = "/axapi/v3/interface/"

    def test_interface_get_list(self):
        # import pdb; pdb.set_trace()
        self.target.get_list()
        self.client.http.request.assert_called_with("GET", self.url_prefix, {}, mock.ANY)

    def test_interface_get(self):
        # import pdb; pdb.set_trace()
        self.target.get()
        self.client.http.request.assert_called_with("GET", self.url_prefix, {}, mock.ANY)

    def _test_interface_create_dhcp(self, dhcp=True):
        expected = 1 if dhcp else 0
        ifnum = 1
        expected_payload = {self.target.iftype: {'ip': {'dhcp': expected}, 'ifnum': ifnum}}
        self.target.create(ifnum, dhcp=dhcp)
        self.client.http.request.assert_called_with("POST", self.url_prefix + str(ifnum),
                                                    expected_payload, mock.ANY)

    def test_interface_create_dhcp_negative(self):
        self._test_interface_create_dhcp(False)

    def test_interface_create_dhcp_positive(self):
        self._test_interface_create_dhcp()

    def test_interface_create_ipaddress_negative(self):
        raise NotImplementedError()

    def test_interface_create_ipaddress_positive(self):
        raise NotImplementedError()

    def test_interface_delete(self):
        raise NotImplementedError()

    def test_interface_update(self):
        raise NotImplementedError()


class TestEthernetInterface(TestInterface):
        def setUp(self):
            super(TestEthernetInterface, self).setUp()
            self.target = interface.EthernetInterface(self.client)
            self.url_prefix = "{0}{1}/".format(self.url_prefix, self.target.iftype)


class TestManagementInterface(TestInterface):
        def setUp(self):
            super(TestManagementInterface, self).setUp()
            self.target = interface.ManagementInterface(self.client)
            self.url_prefix = "{0}{1}/".format(self.url_prefix, self.target.iftype)
