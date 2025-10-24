from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wheelx-sdk",
    version="0.1.0",
    author="WheelX",
    author_email="dev@wheelx.fi",
    description="Python SDK for WheelX quote API and transaction execution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wheelx/wheelx-sdk-python",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "web3": ["web3>=5.0.0"],
    },
    keywords="wheelx, defi, swap, bridge, ethereum, web3",
    project_urls={
        "Bug Reports": "https://github.com/wheelx/wheelx-sdk-python/issues",
        "Source": "https://github.com/wheelx/wheelx-sdk-python",
    },
)