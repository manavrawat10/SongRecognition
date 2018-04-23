from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='SongRecognition',
    url='https://github.com/manavrawat10/SongRecognition',
    author='Manvenddra Rawat',
    author_email='manvenddra.rawat@gmail.com',
    # Needed to actually package something
    packages=['SongRecognization'],
    # Needed for dependencies
    install_requires=['SpeechRecognition','pyaudio','bs4','requests','pywin32', 'lxml'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='Maddy',
    description='Song Recognition will listen to your song lyrics and will result in a song that you can play in youtube as well',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
