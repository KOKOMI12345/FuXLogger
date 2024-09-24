from setuptools import setup, find_packages
from FuXLogger.__metadata__ import __version__ , __author__ , __name__

def load_requirements(filepath: str = "requirements.txt") -> list[str]:
    try:
       with open(filepath, 'r') as f:
           return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
    except Exception:
        return []

setup(
    name=__name__,
    version=__version__,
    packages=find_packages(),
    author=__author__,
    author_email='3072252442@qq.com',
    description='A useful logging library for Python',
    long_description=open('Readme.md','r',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KOKOMI12345/FuXLogger',
    requires=load_requirements(),  # 依赖
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
