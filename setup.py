from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Self Contained Sentiment Analysis App",
    description="A self-contained sentiment analysis application.",
    long_description="This is a self-contained sentiment analysis application that includes all necessary components.",
    version="0.1",
    author="Renswick Delvar",
    author_email="renswick.delver@gmail.com",
    packages=find_packages(include=['src', 'src.*']),
    install_requires = requirements,
)