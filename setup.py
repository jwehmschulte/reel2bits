from setuptools import setup

setup(
    name='reel2bits',
    version='0.1',
    license='MIT',
    python_requires='>=3.6',
    long_description=open('README.md').read(),
    url="http://dev.sigpipe.me/DashieV3/reel2bits",
    author="Dashie",
    author_email="dashie@sigpipe.me",
    install_requires=[
        'Flask',
        'SQLAlchemy',
        'WTForms',
        'WTForms-Alchemy',
        'SQLAlchemy-Searchable',
        'SQLAlchemy-Utils',
        'SQLAlchemy-Continuum',
        'Flask-Bootstrap',
        'Flask-DebugToolbar',
        'Flask-Login',
        'Flask-Mail',
        'Flask-Migrate',
        'Flask-Principal',
        'Flask-Security',
        'Flask-SQLAlchemy',
        'Flask-Uploads',
        'Flask-WTF',
        'bcrypt',
        'pydub',
        'psycopg2-binary',
        'mutagen',
        'unidecode',
        'Flask_Babelex',
        'texttable',
        'python-slugify',
        'python-magic',
        'redis',
        'dramatiq',
        'flask-accept',
        'git+https://github.com/tsileo/little-boxes/'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
