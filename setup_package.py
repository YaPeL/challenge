try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup, find_packages


REQUIREMENTS = parse_requirements("requirements.txt", session=False)

try:  # for pip 20.1
    INSTALL_REQUIRES = [str(r.requirement) for r in REQUIREMENTS]
except AttributeError:  # for pip <= 20.0
    INSTALL_REQUIRES = [str(r.req) for r in REQUIREMENTS]
setup(
    name="challenge",
    version=0.1,
    description="Challenge demo for TruSTAR",
    url="https://github.com/YaPeL/challenge",
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    setup_requires=[],
    tests_require=[],
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.8",
    ],
)
