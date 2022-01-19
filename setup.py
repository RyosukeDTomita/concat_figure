# config: utf-8
from setuptools import setup
from setuptools import find_packages


def main():
    setup(
        name="concatfig",
        version="1.0.2",
        description='concat figure by csvfile order.',
        author="Ryosuke Tomita",
        packages=find_packages(),
        install_requires=[
            "pandas",
            "dataclasses",
            "Pillow",
        ],

        entry_points={
            'console_scripts': [
                'concatfig = concatfig:main',
            ],
        }
    )


if __name__ == "__main__":
    main()
