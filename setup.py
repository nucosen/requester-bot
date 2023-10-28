
# NOTE : To build, use `py setup.py sdist`

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

VERSION = {}

with open("./src/requester-bot/__init__.py") as fp:
    exec(fp.read(), VERSION)

setup(
    name='requester-bot',
    license="MIT License",
    version=VERSION.get("__version__", "0.0.0"),
    description='Requesting system for NUCOSen',
    url='https://github.com/nucosen/requester-bot',
    author='Sitting-cat',
    author_email='info@koaku.ma',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.10, <4',
    install_requires=open(
        "requirements.txt",
        encoding="utf-16"
    ).read().splitlines(),
    entry_points={
        'console_scripts': [
            'requester=requester-bot.cli:execute',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/nucosen/requester-bot/issues',
        'Source': 'https://github.com/nucosen/requester-bot',
    },
)
