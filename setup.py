from setuptools import setup , find_packages

with open("README.md","r",encoding="utf-8")as f:
    long_description = f.read()



setup(
    name="TextSummarization",
    version="0.0.1",
    author="Udayraj Sahu",
    author_email="Udayrajsahu123@gmail.com",
    url=f"https://github.com/Udayraj-Sahu/Text_Summarization"
    ,project_urls={
        "Bug Tracker":f"https://github.com/Udayraj-Sahu/Text_Summarization/issues",
    },
    # install_requires=get_requirements("requirements.txt"),
    package_dir={"":"src"},
    packages=find_packages(where='src')
)