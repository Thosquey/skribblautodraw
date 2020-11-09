import os

import setuptools

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "requests", "__version__.py"), "r", "utf-8") as f:
    # noinspection BuiltinExec
    exec(f.read(), about)

with open("README", "r", "utf-8") as desc:
    readme = desc.read()

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],
    author=about["__author__"],
    author_email=["__author_email__"],
    description=["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=["__url__"],
    license=about["__license__"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment :: Arcade"
    ],
    keywords="skribblio, auto-draw, tool",
    package_dir={"skribblautodraw": "skribblautodraw"},
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/Thosquey/skribblio-auto-draw/issues",
        "Source": "https://github.com/Thosquey/skribblio-auto-draw",
        "Support": "https://github.com/Thosquey?tab=followers",
    },
)