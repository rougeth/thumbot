from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='thumbot',
    version='0.1.0',
    description=('A :thumbsup: and :thumbsdown: counter keyboard for Telegram '
                 'bots and channels'),
    long_description=readme(),
    keywords='telegram bots channels',
    url='https://github.com/rougeth/thumbot',
    author='Marco Rougeth',
    author_email='marco@rougeth.com',
    license='MIT',
    py_modules=['thumbot'],
    install_requires=[
        'pytelegramBotAPI',
        'pymongo',
    ],
)
