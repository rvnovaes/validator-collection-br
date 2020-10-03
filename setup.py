from setuptools import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='validator_collection_br',
    version='0.0.12',
    description=('Validators for common business needs of Brazil'),
    long_description=long_description,
    packages=['validator_collection_br'],
    url='https://github.com/rvnovaes/validator-collection-br',
    license='MIT',
    author='Roberto Vasconcelos Novaes, Luis Guilherme Paim, Iasmini Gomes, Helena Gomes, Germain Pereira',
    author_email='rnovaes@ufmg.br, luis.paimadv@gmail.com, iasmini@silexsistemas.com.br, helena.gomes@silexsistemas.com.br, pereira.germain@outlook.com',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',

        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

    install_requires=[
        'numpy',
        'regex',
        'validator-collection',
    ],

    project_urls={  # Optional
                   'Documentation': 'https://github.com/rvnovaes/validator-collection-br',
                   'Bug Reports': 'https://github.com/rvnovaes/validator-collection-br/issues',
                   'Source': 'https://github.com/rvnovaes/validator-collection-br',
               },
)