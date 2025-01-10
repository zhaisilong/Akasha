from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="akasha",  # Replace with your package name
    version="0.0.1",  # Initial version number
    author="Silong Zhai",  # Replace with your name
    author_email="zhaisilong@outlook.com",  # Replace with your email
    description="A Universe Dataset API in The Field of Drug",  # Short description of the package
    long_description=long_description,  # Long description read from README.md
    long_description_content_type="text/markdown",  # Content type of the long description
    url="https://github.com/zhaisilong/Akasha",  # Replace with your project URL
    packages=find_packages(),  # Automatically find packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Python version requirement
)
