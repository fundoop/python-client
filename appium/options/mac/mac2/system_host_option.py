# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

SYSTEM_HOST = 'systemHost'


class SystemHostOption(SupportsCapabilities):
    @property
    def system_host(self) -> Optional[str]:
        """
        :Returns: The name of the host for the internal server to listen on.
        """
        return self.get_capability(SYSTEM_HOST)

    @system_host.setter
    def system_host(self, value: str) -> None:
        """
        Set the name of the host for the internal server to listen on.
        If not provided then Mac2Driver will use the default host
        address 127.0.0.1. You could set it to 0.0.0.0 to make the
        server listening on all available network interfaces.
        It is also possible to set the particular interface name, for example en1.
        """
        self.set_capability(SYSTEM_HOST, value)