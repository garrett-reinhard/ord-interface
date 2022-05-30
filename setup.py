#! /usr/bin/env python
# Copyright 2020 Open Reaction Database Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Installer script."""

import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='ord-interface',
        description='Interface for the Open Reaction Database',
        url='https://github.com/Open-Reaction-Database/ord-interface',
        license='Apache License, Version 2.0',
        packages=setuptools.find_packages(),
        package_data={
            "ord_interface.visualization": [
                "template.html",
                "template.txt",
            ],
        },
    )
