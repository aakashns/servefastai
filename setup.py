import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="servefastai",
    version="0.1.2",
    author="Aakash N S",
    author_email="opensource@swiftace.ai",
    description="Serve FastAI and get a Web UI with one line of code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aakashns/servefastai",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['flask']
)
