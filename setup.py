from setuptools import setup, find_packages

setup(
    name="text-analyzer-pro-case-study-20260603_160533",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'text=text:main',
        ],
    },
)
