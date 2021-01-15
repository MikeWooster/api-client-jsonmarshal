#!/usr/bin/env python

import setuptools

# Pinning tenacity as the api has changed slightly which breaks all tests.
application_dependencies = ["jsonmarshal"]
prod_dependencies = []
test_dependencies = ["pytest", "pytest-env", "pytest-cov", "vcrpy", "requests-mock", "api-client"]
lint_dependencies = ["flake8", "flake8-docstrings", "black", "isort"]
docs_dependencies = []
dev_dependencies = test_dependencies + lint_dependencies + docs_dependencies + ["ipdb"]
deploy_dependencies = ["requests", "twine"]


with open("README.md", "r") as fh:
    long_description = fh.read()


with open("VERSION", "r") as buf:
    version = buf.read()


setuptools.setup(
    name="api-client-jsonmarshal",
    version=version,
    description="API Client extension for automatic request marshalling.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mike Wooster",
    author_email="",
    url="https://github.com/MikeWooster/api-client-jsonmarshal",
    python_requires=">=3.7",
    packages=["apiclient_jsonmarshal"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    install_requires=application_dependencies,
    extras_require={
        "production": prod_dependencies,
        "test": test_dependencies,
        "lint": lint_dependencies,
        "docs": dev_dependencies,
        "dev": dev_dependencies,
        "deploy": deploy_dependencies,
    },
    include_package_data=True,
    zip_safe=False,
)
