from setuptools import setup

setup(
    name="test-pip-setup-conflict",
    version="0.1.0",
    python_requires=">=3.9",
    install_requires=[
        "requests==2.31.0",
        "Django==2.2.0",
        "flask==2.2.5",
    ],
)
