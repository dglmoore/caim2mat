from setuptools import setup

import sys
if sys.version_info < (3, 5):
    sys.exit('Python3.5 or greater is required')

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='caim2mat',
    python_requires='>=3.5',
    version='1.0.0',
    description='Convert Caim output files to CSV and Excel',
    long_description='',
    long_description_content_type='text/x-rst',
    maintainer='Douglas G. Moore',
    maintainer_email='doug@dglmoore.com',
    url='https://github.com/dglmoore/caim2mat',
    license=LICENSE,
    install_requires=['XlsxWriter'],
    scripts=['caim2mat'],
    test_suite='test',
    platforms=['Windows', 'OS X', 'Linux']
)
