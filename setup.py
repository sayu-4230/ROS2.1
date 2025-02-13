from setuptools import setup
import os
from glob import glob

package_name = 'network_usage'

setup(
    name='network_usage',
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuki Nishijima',
    maintainer_email='s23C1101EC@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'network_usage_pub = network_usage.network_usage_pub:main',
            'listener = network_usage.listener:main',
        ],
    },
)
