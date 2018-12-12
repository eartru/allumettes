# allumettes


## Setup

__required__

  * Python 3.5
  * Virtualenv
  * pip

*For Linux users:*

First check your python3 version

```
python3 -V
```

if it's lower than 3.5 install it.
If you don't have `pip` -> `sudo apt-get install python3-pip`

Then you need virtualenv

```
pip3 install virtualenv
```

*For mac users:*

First you will need `brew` https://brew.sh/2018/01/19/homebrew-1.5.0/ , then:

```
brew install pip3
```
Then you need virtualenv

```
pip3 install virtualenv
```

__virtualenv setup__

In the allumettes directory

```
virtualenv env
source env/bin/activate
pip3 install pygame
pip3 install colorama
```

## Play the game

`python3 main.py`

Inside the game to pick a number of matches:
   with a azerty keyboard:
     - "&" = 1
     - "é" = 2
     - " (just the key " ) = 3
    with any other kind of keyboard
     - "Q" = 1
     - "W" = 2
     - "E" = 3

     To leave the game press "A"

## Benchmark and compare IA

To play with the different kind of IA

`python3 ia_arena.py`

*WARNING: Be careful these algorythm are not optimise and have a heavy cost avoid going higher than 25 matches*