from pickle import FALSE, TRUE
from subprocess import CREATE_NEW_CONSOLE
from tkinter import ROUND

import pyautogui as ag
import pydirectinput as di
from numpy import true_divide
from win32gui import GetForegroundWindow, GetWindowText

DEBUG = TRUE

# left, top, width, and height
HP_STARTX = 40
HP_ENDY = 360
HP_Y = 270

# def canCast(skill):
#     match skill:
#         case 1:
#         case 2:
#         case 3:
#         case 4:
#         case _:


def clearSouthRoute():
    clickImgIfAvailable("img\\centreShip.png", confidence=0.6)
    clickImgIfAvailable("img\\centreShip-2.png", confidence=0.6)
    clickImgIfAvailable("img\\centreShip-3.png", confidence=0.6)


def clearLoot():
    clickImgIfAvailable("img\\gold.png", confidence=0.7)
    clickImgIfAvailable("img\\expOrb.png", confidence=0.7)


def heal():
    if DEBUG:
        print("Healing!")
    di.press('q')


def revive():
    if existsImg("img\\youDied.png"):
        # if existsImg("img\\0RemainingReviveCharge.png"):
        #     clickImg("img\\reviveInTown.png")
        # else:
        clickImg("img\\reviveAtCorpse.png")


def inActionMode():
    return existsImg("img\\bloodInterface.png")
    # return existsImg("img\\bloodInterface.png", region=(0, 0, 400, 305), confidence=0.8)


def inDiablo():
    if GetWindowText(GetForegroundWindow()) == "Diablo Immortal":
        return TRUE
    else:
        return FALSE


def clickImg(img, region=None, confidence=0.8):
    foundLoc = None
    while (foundLoc == None):
        if DEBUG:
            print("Finding: " + img)
        foundLoc = ag.locateOnScreen(
            img, region=region, confidence=confidence, grayscale=True)
        if (foundLoc != None):
            if DEBUG:
                print("Clicking: " + img)
            loc = ag.center(foundLoc)
            ag.click(loc)


def clickImgIfAvailable(img, region=None, confidence=0.8):
    foundLoc = None
    if DEBUG:
        print("Finding: " + img)
    foundLoc = ag.locateOnScreen(
        img, region=region,  confidence=confidence, grayscale=True)
    if (foundLoc != None):
        if DEBUG:
            print("Clicking: " + img)
        loc = ag.center(foundLoc)
        ag.click(loc)


def waitImg(img, region=None, confidence=0.8):
    foundLoc = None
    while (foundLoc == None):
        if DEBUG:
            print("Finding: " + img)
        foundLoc = ag.locateOnScreen(
            img, region=region,  confidence=confidence, grayscale=True)
        if (foundLoc != None):
            if DEBUG:
                print("Found: " + img)


def existsImg(img, region=None, confidence=0.8):
    foundLoc = ag.locateOnScreen(
        img, region=region,  confidence=confidence, grayscale=True)
    if (foundLoc != None):
        if DEBUG:
            print("Found: " + img)
            print(foundLoc)
        return True
    else:
        if DEBUG:
            print("Not Found: " + img)
        return False


def estimateHP():
    for HPX in range(HP_STARTX, HP_ENDY, 20):
        if ag.pixelMatchesColor(HPX, 270, (0, 0, 0), 70):
            estimatedHP = round(((HPX - HP_STARTX) / HP_ENDY) * 100, 0)
            print("HP: " + str(estimatedHP) + "%")
            return estimatedHP

    return 100
