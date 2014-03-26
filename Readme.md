# GistPy

Small python script that creates a new anonymous gist at [gist.github.com](https://gist.github.com/) with content coming from
stdin

## TODO

[See issues](https://github.com/aseba/GistPy/issues)

## How to install:

```bash
curl -s https://raw.github.com/aseba/GistPy/master/GistPy > GistPy
chmod 755 GistPy
mv GistPy /usr/local/bin/GistPy
```

Ti configure GistPy executing GistPy once and follow the steps on screen.

You can use your username and password or a [username and access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use)

```bash
GistPy
```

If you want to reconfigure it in the future, you can execute

```bash
GistPy --reconfigure
```

## Usage
```bash
GistPy < file
```

or

```bash
cat file | GistPy
```

or even more useful in mac

```bash
pbcopy | GistPy
```

## Options
* --name -n: Sets the name for the file
* --description -d: Sets the description for the gist
* --open -o: Opens the url returned by github using the command `open` (Mac Only I suppose)
* --private -p: Creates the gist as private

Example:
```bash
cat GistPy | GistPy -n "GistPy" -d "Small python script that creates a new anonymous gist with content coming from stdin" -o -p -U aseba -P shhthisisasecret
```

## OSX Service

I've created an automator service `GistPy` that will add a service that you can execute using a keybinding.

### Installation

Double click `GistPy.workflow` in your mac

### Keyboard Shortcut

After you've installed the service, you should go to `system preferences > keyboard > shortcuts` and in the left pane select `Services`

You should find in the `General` section the service `GistPy`, click in `add a shortcut` and add a shortcut. That is it

### Security

If you've configured your username and password in GistPy you'll create private gists, if not, all gists are going to be public
