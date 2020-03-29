import os, sys

import setuptools

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setuptools.setup(
    name="magmatar-api", # Replace with your own username
    version="1.0-rc2",
    author="Snavy",
    author_email="1337Snavy@gmail.com",
    description="Public Magmatar.com API Wrapper",
    long_description="Public Magmatar.com API Wrapper",
    long_description_content_type="text/markdown",
    url="https://github.com/Snavyy/magmatar-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
