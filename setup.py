from setuptools import setup, find_packages

setup(
    name="looprint",
    version="0.1.0",
    author="Jonathan Lombardo",
    author_email="jonathanlombardo90@gmail.com",
    description="Simplify printing loops progress",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jonathanlombardo/terminal",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # ...
    ],
)
