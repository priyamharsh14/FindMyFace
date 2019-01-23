# FindMyFace
A face recognition tool written in Python3 implementing image processing and multi-threading

## Installation:

```
$ git clone https://github.com/priyamharsh14/FindMyFace.git
```

Change the directory -
```
$ cd FindMyFace
/FindMyFace/$
```

Install the required Python modules -
```
/FindMyFace/$ pip install -r requirements.txt
```
__NOTE: For Windows User, you also need Microsoft Visual Studio Build Tools to install the required Python modules__


## Usage:

Start with registering your face -
```
/FindMyFace/$ python register_my_face.py
********** Register Your Face **********

Enter your name: <Your Name>

Getting the camera ready..

Press Space whenever ready..
Press Esc to cancel the registration..
```

After successfull registration, your face will be saved inside a folder named 'Registered'.

Let's see the help menu by typing -
```
/FindMyFace/$ python find_my_face.py --help
  ______ _           _   __  __         ______
 |  ____(_)         | | |  \/  |       |  ____|
 | |__   _ _ __   __| | | \  / |_   _  | |__ __ _  ___ ___
 |  __| | | '_ \ / _` | | |\/| | | | | |  __/ _` |/ __/ _ \
 | |    | | | | | (_| | | |  | | |_| | | | | (_| | (_|  __/
 |_|    |_|_| |_|\__,_| |_|  |_|\__, | |_|  \__,_|\___\___|
                                 __/ |
                                |___/              ver. 1.2

Author: Priyam Harsh

Usage: find_my_face.py path

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit
```

In order to run this program, type this -
```
/FindMyFace/$ python find_my_face.py <path to any folder containing pictures>
```

This tool will process all the pictures inside the provided folder and if any pictures contains your face, it will be copied to a folder named 'my_pictures'.
