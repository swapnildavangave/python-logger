import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-logger",
    version="0.0.1",
    author="Swapnil Davangave",
    author_email="swapnildavan11@gmail.com",
    description="Custom multi instance logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swapnildavangave/python-logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)