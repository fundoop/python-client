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

SYSTEM_PORT = 'systemPort'


class SystemPortOption(SupportsCapabilities):
    @property
    def system_port(self) -> Optional[int]:
        """
        :Returns: The number of the port for the internal server to listen on.
        """
        return self.get_capability(SYSTEM_PORT)

    @system_port.setter
    def system_port(self, value: int) -> None:
        """
        Set the number of the port for the internal server to listen on.
        If not provided then Mac2Driver will use the default port 10100.
        """
        self.set_capability(SYSTEM_PORT, value)