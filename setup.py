import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wrapmediannfo',
    version='0.1',
    scripts=['wrapmediainfo'],
    author="Supermasita",
    author_email="supermasita@supermasita.com",
    description="A simple Python wrapper for Mediainfo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/supermasita/wrapmediainfo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX :: Linux",
    ],

)
