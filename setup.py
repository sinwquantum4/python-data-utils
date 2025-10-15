from setuptools import setup, find_packages

setup(
    name="data-utils",
    version="0.1.0",
    description="Simple data utilities library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black",
            "flake8",
        ],
    },
    python_requires=">=3.8",
)