#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open('requirements.txt', 'r') as f:
    install_reqs = [
        s for s in [
            line.strip(' \n') for line in f
        ] if not s.startswith('#') and s != ''
    ]

import setuptools

setuptools.setup(
    name='mtg-nn',
    version='1.0',
    packages=setuptools.find_packages(),
    entry_points={},
    install_requires=install_reqs,
)
