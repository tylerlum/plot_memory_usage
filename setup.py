from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.0.1"
DESCRIPTION = (
    "Create a live plot of the CPU or GPU memory usage of your system over time"
)
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="plot_memory_usage",
    version=VERSION,
    author="Tyler Lum",
    author_email="tylergwlum@gmail.com",
    url="https://github.com/tylerlum/plot_memory_usage",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["live-plotter", "tyro", "GPUtil", "psutil"],
    keywords=["python", "plot", "memory", "usage", "cpu", "gpu"],
    entry_points={
        "console_scripts": [
            "plot_memory_usage=plot_memory_usage.plot_memory_usage_core:main",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
