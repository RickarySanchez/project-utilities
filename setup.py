import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="project-utilities",
    version="1.0.1",
    description="A package containing scripts, classes, functions etc all useful for maintaining projects",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/RickarySanchez/project-utilities",
    author="RickarySanchez",
    author_email="RickarySanchez@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["project_utilities"],
    include_package_data=True,
    install_requires=["PyYAML"],
)
