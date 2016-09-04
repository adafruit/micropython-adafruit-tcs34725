from distutils.core import setup


setup(
    name='Adafruit-upy_tcs34725',
    py_modules=['tcs34725'],
    version="1.0",
    description="Driver for MicroPython for the tcs34725 RGB sensor.",
    long_description="""\
This library lets you communicate with a TCS34725 RGB sensor.
""",
    author='Radomir Dopieralski',
    author_email='micropython@sheep.art.pl',
    classifiers = [
        'Development Status :: 6 - Mature',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
