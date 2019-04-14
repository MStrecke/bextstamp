# Informations for programmers

This is my first venture into the realm of Applescript. If you know of any better workflow than the one described in README.md which is available on a normal maschine please let me know.

This project demonstrates how to make a droplet and combine it with a small python script.

## bextstamp.py

### Why Python 2?

This utility uses the soon to be deprecated Python 2 because this version is preinstalled.

### How it works

The `bext` chunk is usually the first one in a Broadcast Wave file. This means the information can be found at a fixed position within the file  which makes it unnecessary to write a RIFF chunk decoder.

The utility checks a few magic values, extracts the date string, converts it to a Unix timestamp and modifies the file.

### Return codes

| Code | Remark |
|:----:| ------ |
| 0 | no problems |
| 1 | filename missing |
| 2 | file open error |
| 3 | conversion error |
| 4 | error modifying the file |

## bextstamp.applescript

This part implents the two events used by droplets.

To make the droplet portable the Python script has to be manually copied into the `Contents/Resources` folder of the app created by the Script Editor.

### Good to know

The value returned by `path to resource` has to be converted into a POSIX path in order to be used by `do shell`:

```Applescript
set mypro to POSIX path of (path to resource "bextstamp.py")
do shell script ("python " & mypro & " " & this_item)
```

## Useful links

* Broadcase Wave Specification - <https://tech.ebu.ch/docs/tech/tech3285.pdf>
* <http://bitmuncher.subnetworx.de/2014/02/04/ein-droplet-fuer-macosx-erstellen/>
* <https://apple.stackexchange.com/questions/157724/applescript-path-to-files-in-applications-resources>