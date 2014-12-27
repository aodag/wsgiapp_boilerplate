from setuptools import setup
import os


__version__ = '0.1'
__author__ = 'Atsushi Odagiri'
__email__ = 'aodagx@gmail.com'
here = os.path.dirname(__file__)

requires = [
]

tests_require = [
    "webtest",
]


def _read(name):
    with open(os.path.join(here, name)) as f:
        return f.read()

setup(
    name="wsgiapp_boilerplate",
    version=__version__,
    license='MIT',
    author=__author__,
    author_email=__email__,
    description="boilerplate for wsgi application.",
    long_description=_read("README.rst"),
    packages=["webapp"],
    test_suite="webapp",
    url="https://github.com/aodag/wsgiapp_boilerplate",
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
)
