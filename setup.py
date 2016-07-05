"""
Wiuppy, the Where's It Up API Python library.

"""

from setuptools import setup, find_packages


setup(
    name="wiuppy",
    version="0.0.1",
    author="ellotheth",
    description="Where's It Up Python API bindings.",
    packages=find_packages(),
    long_description=__doc__,
    zip_safe=False,
    install_requires=[
        'requests>=2.10'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
