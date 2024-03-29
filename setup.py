import os
import setuptools

def requirements():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), encoding="utf-8") as f:
        return f.read().splitlines()

def package_files(directory):
    paths = []
    print(list(os.walk(directory)))
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    print(paths)
    return paths

setuptools.setup(
    name="ivete",
    version="1.0.0",
    license="MIT",
    author="Seongbum Seo",
    author_email="sbumseo@bigpicture.team",
    description="End-to-Inference Machine Learning Framework",
    long_description=open("README.md").read(),
    url="https://github.com/bigpicture-kr/ivete",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "": package_files("ivete/deploy/templates")
    },
    zip_safe=True,
    install_requires=requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
