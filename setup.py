import setuptools, os

readme_path = os.path.join(os.getcwd(), "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r") as f:
        long_description = f.read()
else:
    long_description = 'kpublicip'

setuptools.setup(
    name="kpublicip",
    version="0.0.2",
    author="Kristof",
    description="get your public ipv4 or ipv6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkristof200/py_public_ip",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)