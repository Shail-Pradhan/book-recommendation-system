from setuptools import setup

with open ('README.md', 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",  
    version="0.1.0",  
    author="Shail",
    author_email="shailprd69@gmail.com",
    description="Packages for Books Recommendation System",
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    packages=["src"], 
    license="MIT",
    python_requires=">=3.6",  
    install_requires=['streamlit','numpy']
)

