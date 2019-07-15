from setuptools import setup
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'innov'))
from config import __version__, __github_username__, __github_reponame__

url = 'https://github.com/' + __github_username__ + '/' + __github_reponame__

setup(
    name='innov',
    version=__version__,
    url=url,
    license='Apache 2.0',
    author='Max Solutions, Co',
    packages=['innov'],
    author_email='dev@max-solutions.co',
    description='Python SDK for the Max Solutions Co API',
    install_requires=[
        'requests>=2.11.1',
        'simplejson>=3.16.0'
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating system :: OS Independent',
        'Programming language :: Python',
        'Topic :: Software development :: Libraries :: Python Modules'
    ],
    keywords=[
        'sdk',
        'invoice',
        'subscription'
    ]
)
