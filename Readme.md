# GistPy

GistPy is a small python script that creates a new anonymous (or not) gist at [gist.github.com](https://gist.github.com/) with content coming from stdin.

It also has an [Automator Script](#osx-service) for mac to be able to bind the process to a keystroke and paste gists directly from the content of the clipboard.

## TODO

[See issues](https://github.com/aseba/GistPy/issues)

## How to install:

```bash
curl -Ls https://raw.github.com/aseba/GistPy/master/GistPy > GistPy
chmod 755 GistPy
mv GistPy /usr/local/bin/GistPy
```

To configure GistPy execute GistPy once and follow the steps on screen.

You can use your username and password or a [username and access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use).

```bash
GistPy
```

If you want to reconfigure it in the future, you can execute

```bash
GistPy --reconfigure
```

## Usage
```bash
~ GistPy < file

or

~ cat file | GistPy
```

Or even more useful in mac to create a gist with the content of your clipboard

```bash
LANG=en_US.UTF-8 pbpaste | GistPy
```

`LANG=en_US.UTF-8` is to force UTF-8 in case you have weird characters copied in your clipboard

Also, you can create a gist and copy the URL to the clipboard

```bash
cat file | GistPy | pbcopy
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

I've created an automator service `GistPy` that will add a service that you can execute using a keybinding in order to create a gist with the content of the clipboard.

It just executes the command `pbpaste | GistPy -p -o | pbcopy`.

### Installation

Double click `GistPy.workflow` in your mac and click *Install*

### Keyboard Shortcut

After you've installed the service, you should go to `system preferences > keyboard > shortcuts` and in the left pane select `Services`

In the `General` section You should find the service `GistPy`, click in `add a shortcut` and create one. That is it.

### Security

If you've configured your username and password in GistPy you'll create private gists, if not, all gists are going to be public and anonymous.
