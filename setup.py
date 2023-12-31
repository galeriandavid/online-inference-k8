from setuptools import setup, find_packages

setup(
    name='hw_pp',
    version='0.1.11',
    description="A small example package for iris prediction app",
    classifiers = [
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/galeriandavid/online-inference-k8',
    author='David',
    author_email='galeriandavid@gmail.com',
    license='MIT',
    packages=find_packages(),
    requires=[
        "pandas==2.0.3",
        "anyio==3.6.1",
        "pydantic==1.10.12",
        "fastapi[all]==0.85.2",
        "scikit-learn==1.3.2"
    ],
    install_requires=[
        "pandas==2.0.3",
        "anyio==3.6.1",
        "pydantic==1.10.12",
        "fastapi[all]==0.85.2",
        "scikit-learn==1.3.2"
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': ['iris=hw_pp.app.server:main']
    }
)