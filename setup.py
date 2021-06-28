from setuptools import setup, find_packages

# See note below for more information about classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="simpcalc",
    version="0.0.1",
    description="A lib",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Harukomaze/simpcalc",
    author="Harukomaze",
    author_email="sdpqwer0@gmail.com",
    license="MIT",  # note the American spelling
    classifiers=classifiers,
    keywords="discord discord-calc calculator easy-calc simple-calculator discord.py",  # used when people are searching for a module, keywords separated with a space
    packages=find_packages(),
    install_requires=[
        "aiohttp", "urllib3"
    ],  # a list of other Python modules which this module depends on.  For example RPi.GPIO
    include_package_data=True
)
