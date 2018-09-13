from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'LICENSE'), encoding='utf-8') as f:
    long_description += f.read()

with open(path.join(here, 'atoma', 'const.py'), encoding='utf-8') as fp:
    version = dict()
    exec(fp.read(), version)
    version = version['VERSION']

setup(
    name='atoma',
    version=version,
    description='Atom, RSS and JSON feed parser for Python 3',
    long_description=long_description,
    url='https://github.com/NicolasLM/atoma',
    author='Nicolas Le Manchet',
    author_email='nicolas@lemanchet.fr',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    keywords='atom rss json feed feeds syndication parser RFC4287',

    packages=find_packages(include=('atoma', 'atoma.*')),
    install_requires=[
        'defusedxml',
        'attrs',
        'python-dateutil'
    ],

    extras_require={
        'tests': [
            'pytest',
            'pytest-cov',
            'python-coveralls',
            'pycodestyle'
        ]
    }
)
