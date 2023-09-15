import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = 'text_summator'
AUTHOR_USER_NAME = 'themjdex'
SRC_REPO = 'textSummator'
AUTHOR_EMAIL = 'themjdex@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Example text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)