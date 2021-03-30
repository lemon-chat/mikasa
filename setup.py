
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mikasa", # Replace with your own username
    version="0.0.1",
    author="Jun Wang",
    author_email="jstzwj@aliyun.com",
    description="Mikasa QQ bot framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lemon-chat/mikasa",
    project_urls={
        "Bug Tracker": "https://github.com/lemon-chat/mikasa/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': [
            'mikasa-admin = mikasa.admin:main',
        ]
    }
)