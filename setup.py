import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="distancia", 

    version="0.0.1",

    author="Yves Mercadier",

    author_email="",

    description="distance metrics",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/ym001/distancia",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.0',

)
