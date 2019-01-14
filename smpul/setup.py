import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smpul",
    version="0.",
    author="Alex Hall",
    author_email="bearodark@gmail.com",
    description="A small set of tools to make Python just a bit easier to use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ultrabear/smpul-src-code",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)