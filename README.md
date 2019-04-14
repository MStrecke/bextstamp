# bextstamp

bextstamp is a Mac OSX droplet which sets the filedate of a broadcast WAV file to the date stored in the file's BEXT chunk.

It conists of an Applescript file that calls a small python script which in turn analyses the WAV file and modifies the file modification date.

## Installation

As mentioned above the utility consists of two parts:

* an Applescript handling the droplet
* a Python script analyzing and modifying the WAV file.

The Applescript has to be compiled using Apple`s Script Editor.
The Python script has than to be copied into the compiled app.

* Open `bextstamp.applescript` with Apple's Script Editor.
* Export it as `program`.
  * This will create `bextstamp.app` at the location of your choosing.
* Right click `bextstamp.app` and open it with `Show Package Contents`.
  * Go to its `Contents/Resources` subfolder and copy `bextstamp.py` into that subfolder.

The droplet is now good to go and can be copied to other locations .
