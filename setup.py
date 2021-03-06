import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ho-hello", # Replace with your own username
    version="0.0.1",
    author="amansman77",
    author_email="amansman77@gmail.com",
    description="Hello package for Ho",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amansman77/practice-python-packaging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)