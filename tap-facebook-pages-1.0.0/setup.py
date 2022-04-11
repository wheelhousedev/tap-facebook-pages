# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_facebook_pages']

package_data = \
{'': ['*'], 'tap_facebook_pages': ['schemas/*']}

install_requires = \
['requests>=2.27.1,<3.0.0', 'singer-sdk==0.4.4']

entry_points = \
{'console_scripts': ['tap-facebook-pages = tap_facebook_pages.tap:cli']}

setup_kwargs = {
    'name': 'tap-facebook-pages',
    'version': '1.0.0',
    'description': '`tap-facebook-pages` is Singer-compliant facebook-pages tap built with Singer SDK.',
    'long_description': None,
    'author': 'Egi Gjevori',
    'author_email': 'egi.gjevori@y42.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
