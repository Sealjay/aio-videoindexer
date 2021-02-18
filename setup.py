import pathlib
from setuptools import setup


CURRENT_PATH = pathlib.Path(__file__).parent
README_TEXT = (CURRENT_PATH / "README.md").read_text()

setup(
    name="aio-videoindexer",
    version="0.1.0",
    description="An async video indexer package for querying Microsoft Media Services Video Indexer in Python.",
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    url="https://github.com/Sealjay-clj/aio-videoindexer",
    author="Chris Lloyd-Jones",
    license="MIT",
    packages=["aiohttp", "aiohttp[speedups]"],
    zip_safe=False,
)
