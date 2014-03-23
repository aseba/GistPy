# gist.py

Small python script that creates a new anonymous gist at [gist.github.com](https://gist.github.com/) with content coming from
stdin

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

## Options
* --name -n: Sets the name for the file
* --description -d: Sets the description for the gist
* --open -o: Opens the url returned by github using the command `open` (Mac Only I suppose)
* --private -p: Creates the gist as private
* --username -U: Logins to github.com with this username
* --password -P: Logins to github.com with this password

Example:
```bash
cat gist.py | gist.py -n "gist.py" -d "Small python script that creates a new anonymous gist with content coming from stdin" -o -x -u aseba -p shhthisisasecret
```

