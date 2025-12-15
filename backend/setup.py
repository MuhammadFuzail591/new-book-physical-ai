"""Setup file for the RAG Pipeline package."""

from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the contents of requirements file
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="rag-pipeline",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="RAG Pipeline for ingesting content from Vercel-deployed book website, generating embeddings, and storing in Qdrant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/rag-pipeline",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.23.0",
            "pytest-cov>=4.1.0",
            "black>=23.10.0",
            "flake8>=6.0.0",
            "mypy>=1.7.0",
            "isort>=5.12.0",
            "pre-commit>=3.5.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "rag-pipeline=src.rag_pipeline.main:main",
        ],
    },
)