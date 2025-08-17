from setuptools import setup, find_packages

setup(
    name="mypkg-janiramimariquesi",
    version="0.1.0",
    author="Mario Cristales",
    description="Demo de paquete para taller GitHub Actions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
)
