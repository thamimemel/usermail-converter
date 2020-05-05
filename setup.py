from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = "1.0"
setup(
  name = 'usermail-converter',
  packages = ['usermail-converter'],
  version = version,
  license='GPLv3',
  description = 'A Python Cross Platform GUI App Tool to Convert Between Emails and Usernames',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Thami Memel',
  author_email = 'memelthami@gmail.com',
  url = 'https://github.com/ThamiMemel/UserMail_Converter',
  download_url = f'https://github.com/ThamiMemel/usermail-converter/archive/{version}.tar.gz',
  keywords = ['username', 'email', 'mail', 'converter', "combo"],  
  install_requires=[ 
          'pyqt5==5.14.2',
          'PyAutoGUI==0.9.50',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable', #"3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: End Users/Desktop',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    "Topic :: Utilities",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS",
    "Operating System :: Microsoft :: Windows",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8"
  ],
  entry_points={
    'console_scripts': [
        'usermail_converter=usermail_converter.__main__:main',
        ],
    },
  package_data={'usermail_converter': ['icons/*']},
)