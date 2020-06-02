The ddlcWiki module for Python 3
================================

NOTICE: This module is no longer worked on (at all) and has been archived, the PyPi version of this module has been removed and I no longer accept issue requests on this anymore.

#### Made by stshrewsburyDev

Installation:
-------------

###### Install with pip: (No longer working use the Install from source method)

```
```

###### Install from source:

```
python setup.py install
```

ChangeLogs:
-----------

* Fixed the info on the help command on the module (``help(ddlcWiki)``)
* Updated the image URL's to the new ones

Using in your code:
-------------------

###### Import the module:

```py
import ddlcWiki
```

###### Functions:

```py
ddlcWiki.ListCharacters()
# Outputs a list of the characters

ddlcWiki.GetAllInfo(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a JSON library with all the character info

ddlcWiki.GetAge(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a integer age of the character

ddlcWiki.GetPoemFont(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a string name of the characters poem font

ddlcWiki.GetHeight(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a string height of the character

ddlcWiki.GetHairColour(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a string hair colour of the character

ddlcWiki.GetEyeColour(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a string eye colour of the character

ddlcWiki.GetImgNormal(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a string URL image of the character

ddlcWiki.GetImgChibi(character)
# character must be one from the ListCharacter list (non case sensitive)
# Outputs a string URL image of the character
```

Links:
------

* [GitHub repository page](https://github.com/stshrewsburyDev/ddlcWiki)
* [The stshrewsburyDev official site](https://stshrewsburydev.github.io/)
