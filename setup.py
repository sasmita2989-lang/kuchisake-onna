from setuptools import find_packages, setup

setup(
    name="kuchisake-onna",
    version="1.0.0",
    description="A Python library inspired by Kuchisake-onna",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
)
