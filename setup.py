import setuptools
with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

setuptools.setup(
    name="genie-core-jeremi1995",
    version="0.0.1",
    author="Jeremy Duong",
    author_email="jeremibq@gmail.com",
    description="A small example calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": ""},
    packages=setuptools.find_packages(),
    python_requires=">=3.9.7",
    install_requires=[]        # List dependencies of this project
)