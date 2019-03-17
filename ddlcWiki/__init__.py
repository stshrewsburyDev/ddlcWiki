"""
ddlcWiki (Doki doki literature club Python wiki API)
Made by stshrewsburyDev
"""

import ddlcWiki.data as data


def ListCharacters():
    """
    Lists the characters names from the game.
    Also shows the key names for the other commands.
    :return: List of names
    """
    return ["Sayori", "Yuri", "Natsuki", "Monika", "MC"]


def GetAllInfo(character=None):
    """
    Shows the full info of the character entered.
    :param character: String name of a character
    :return: JSON library of all info on inputted character
    """
    if character is None:
        raise NameError("GetAllInfo() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetAge(character=None):
    """
    Shows the age of the character entered.
    :param character: String name of a character
    :return: Integer age of the inputted character
    """
    if character is None:
        raise NameError("GetAge() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["Age"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetPoemFont(character=None):
    """
    Shows the poem font of the character entered.
    :param character: String name of a character
    :return: String poem font name from the inputted character
    """
    if character is None:
        raise NameError("GetPoemFont() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["PoemFont"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetHeight(character=None):
    """
    Shows the height of the character entered.
    :param character: String name of a character
    :return: String height of the inputted character
    """
    if character is None:
        raise NameError("GetHeight() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["Height"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetHairColour(character=None):
    """
    Shows the hair colour of the character entered.
    :param character: String name of a character
    :return: String hair colour of the inputted character
    """
    if character is None:
        raise NameError("GetHairColour() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["HairColour"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetEyeColour(character=None):
    """
    Shows the eye colour of the character entered.
    :param character: String name of a character
    :return: String eye colour of the inputted character
    """
    if character is None:
        raise NameError("GetEyeColour() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["EyeColour"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetImgNormal(character=None):
    """
    Shows the normal image URL of the character entered.
    :param character: String name of a character
    :return: String URL image of the inputted character
    """
    if character is None:
        raise NameError("GetImgNormal() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["ImgNormal"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))


def GetImgChibi(character=None):
    """
    Shows the chibi image URL of the character entered.
    :param character: String name of a character
    :return: String URL image of the inputted character
    """
    if character is None:
        raise NameError("GetImgChibi() expected a character name but received {0}".format(character))
    else:
        try:
            return data.CharacterInfo["{0}Info".format(character.lower())]["ImgChibi"]
        except:
            raise NameError("Unknown name entered ({0}), use ListCharacters() to see the list of names you can enter".format(character))
