# SimpleEmail_SpamBot
Just a simple email spam bot written in Python. The respositroy name says it all.

## A little update:
0. 0.8 is indeed coming. I'm not going to delete this repo, heh.
1. I might change the name later. Because I'll make it an email client.
2. I'll add a GUI as well. An email client with CLI and GUI.
3. 0.8 fixes some stuff too.

Also, It seems like someone has forked this repo. I don't know why or what they're going to do with it, but cool :3.

### KNOWN ISSUES:
1. whoops
```python
elif command == "set message":
    try:
        # yes.
        spam_subject = raw_input("\nMESSAGE>>> ")

    except KeyboardInterrupt:
        print("\nStopped.")

    except EOFError:
        print("\nStopped.")

    self.command_line()
            
```
2. uh yeah

```python
print("\nDELAY SET TO: %d" % spam_delay)
TypeError: %d format: a number is required, not str
```

### What will happen to SESB?
I do not know lel. I will add some new stuff later, just working on something else.

```SESB.py``` = ```v0.7```
[See what's new.](https://github.com/DizAzTor/SimpleEmail_SpamBot/blob/master/SESB/changelog.txt)


#### This only works with Python 2.x (I'll fix that in the future)
#### DOWNLOAD AS .ZIP

#### Windows:
0. [**Download compiled .exe files**](https://github.com/DizAzTor/SimpleEmail_SpamBot/releases/tag/v0.7)

_Or you can run the script through Python_:

0. Go to where you downloaded the zip file and unzip it.
1. Go to "SimpleEmail_SpamBot"
2. Open "SESB"~~
3. Configure ```config.cfg```.~~
4. Open a terminal in that location.
5. Type ```C:\Python27\python.exe SESB.py``` in the terminal and press ENTER.

#### You can add ```alias python=python2``` and ```alias python3=python3``` to your ```.bashrc``` file.

#### Linux / MacOS
0. ```cd ~/Downloads```
1. ```unzip SimpleEmail_SpamBot-master.zip```
2. ```cd SimpleEmail_SpamBot-master/SESB/```
3. Configure ```config.cfg```.
4. ```python SESB.py```

#### TO USE MANUAL MODE:
* Run the script with **-m**
* For an example, ```python SESB.py -m```

#### TO USE COMMAND MODE:
* Run the script with **-c**
* For an example, ```python SESB.py -c```

### ELSE:
* Config config.cfg and the script will run using your settings.
