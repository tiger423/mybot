from setuptools import setup, find_packages
setup(
    name="mybot",
    version="2.0.0",
    packages=find_packages(where="core"),
    package_dir={"": "core"},
    entry_points={"console_scripts": ["mybot=mybot_core.main:main"]},
    install_requires=["openai", "playwright"],
)
