import os
from setuptools import setup, find_packages

BUILD_ID = os.environ.get("BUILD_BUILDID", "0")

setup(
    name="deep_timeit",
    version="0.1" + "." + BUILD_ID,
    # Author details
    author="Oliver Gibson",
    author_email="ojrgibson@perse.co.uk",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["matplotlib"],
)