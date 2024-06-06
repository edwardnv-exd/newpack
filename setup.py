from setuptools import setup, find_packages

setup (
    name = "hello_package",
    version = "1",
    packages = find_packages (),
    install_requires = [],
    url = "https://github.com/edwardnv-exd/newpack",
    author = "Edward",
    author_email = "edward_nv@exdion.com",
    description = "Another simple hello package"
)