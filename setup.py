from setuptools import setup, find_packages

setup(
    name="user_age_analyzer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.4",
    ],
    extras_require={
        "dev": [
            "pytest>=8.4.1",
        ],
    },
    author="Pankaj Baviskar",
    author_email="pankaj_baviskar@hotmail.com",
    description="A Python application that analyzes user age data from Random User API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pankajbbaviskar/user-age-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
)
