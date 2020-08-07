import setuptools
import shutil
import os

setuptools.setup(
    name="HARK-TF-PARSER",
    version="0.1",
    author="Ryosuke Kojima",
    author_email="kojima.ryosuke.8e@kyoto-u.ac.jp",
    description="HARK transfer function library",
    long_description="A python library to read/parse transfer function files with .zip extention used in HARK, a robot audition open source tool",
    long_description_content_type="text/markdown",
    url="https://github.com/kojima-r/HARK_TF_Parser",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "hark_tf_mat= hark_tf.read_mat:main",
            "hark_tf_param= hark_tf.read_param:main",
       ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
