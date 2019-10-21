import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="osrsslayertool",
    version="0.0.5",
    author="James Cerniglia",
    author_email="cerniglj1@hawkmail.newpaltz.edu",
    description="A package for developers or players to use to visualize what they can do with the slayer skills on Old School Runescape. The tool can be used to see graphs of which task the player wil most likely receive (create_graph() method). The user can see what tasks they can do at their current stats (get_doable_assignments()). This does not calculate quests yet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cerniglj1/osrsslayertool",
    packages=setuptools.find_packages(),
    download_url = 'https://github.com/cerniglj1/osrsslayertool/archive/master.zip',
    keywords = ['OSRS', 'Runescape', 'Old School Runescape','Old','School','Runescape','2007scape','2007Scape',],
    classifiers=[
        'Intended Audience :: Developers :: Players',     
        'Topic :: Software Development :: Build Tools',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)