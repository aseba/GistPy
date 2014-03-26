# gist.py

Small python script that creates a new anonymous gist at [gist.github.com](https://gist.github.com/) with content coming from
stdin

## TODO

- [Better security. Password in plain text in the script sucks](https://github.com/aseba/GistPy/issues/1)
- [Automator path is hardcoded](https://github.com/aseba/GistPy/issues/2)
- [from-pastebin.sh has a hardcoded path to the script](https://github.com/aseba/GistPy/issues/3)

## How to install:

```bash
curl -s https://raw.github.com/aseba/GistPy/master/gist.py > gist.py
chmod 755 gist.py
```
optional:
```bash
cp gist.py /usr/local/bin/gist.py
```

## Usage
```bash
gist.py < file
```

or

```bash
cat file | gist.py
```

or even more useful in mac

```bash
pbcopu | gist.py
```

## Options
* --name -n: Sets the name for the file
* --description -d: Sets the description for the gist
* --open -o: Opens the url returned by github using the command `open` (Mac Only I suppose)
* --private -p: Creates the gist as private
* --username -U: Logins to github.com with this username
* --password -P: Logins to github.com with this password

Example:
```bash
cat gist.py | gist.py -n "gist.py" -d "Small python script that creates a new anonymous gist with content coming from stdin" -o -p -U aseba -P shhthisisasecret
```

## OSX Service

I've created an automator service that calls `from-pastebin.sh`. 

If you bind that automator script to a keybinding in your mac, you can have a quick keybinding to post gists in github ;)

