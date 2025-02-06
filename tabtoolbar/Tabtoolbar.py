# Author-
# Description-

import adsk.core
import adsk.fusion
import adsk.cam
import os
import traceback
import pathlib
import zipfile
import json
import urllib.request
from sys import platform

# import adsk.cam

# Initialize the global variables for the Application and UserInterface objects.
app = adsk.core.Application.get()
ui = app.userInterface

# Check if the user is wants production on insider toolbars. DEFAULT is Production (false)
tbnext = False  # get the current production toolbars

if tbnext == True:
    gitPrefix = f"https://raw.githubusercontent.com/schneik80/Fusion-Assembly-Tab/next/"
else:
    gitPrefix = f"https://raw.githubusercontent.com/schneik80/Fusion-Assembly-Tab/main/"

tbURL = f"{gitPrefix}newbars/design/TabToolbars.xml"  # URL to the main branch in GITHUB for the new tabtoolbar.xml
fpURL = f"{gitPrefix}newbars/flatpattern/TabToolbars.xml"  # URL to the main branch in GITHUB for the new flat pattern tabtoolbar.xml
pmURL = f"{gitPrefix}newbars/mesh/TabToolbars.xml"  # URL to the main branch in GITHUB for the new mesh tabtoolbar.xml


# main script
def run(context):

    # Prompt user to run or exit
    ui.messageBox(
        "Click YES, to install a new Design Document Toolbar with a dedicated Assembly Tab?\n\nA backup of your existing toolbar xml will be created automatically. ",
        "Install Assembly Tab",
        3,
        1,
    )

    # Detect the OS platform so we can get the correct path to the tabtoolbar.xml
    try:
        swapXML(platform)

        ui.messageBox(
            "New Design toolbar with Assembly Tab is installed. Please save and close or close all open documents then restart Fusion",
            "Install Assembly Tab",
            0,
            2,
        )

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


# Windows
def swapXML(OS):
    try:

        PATHS_DICT = json.loads(app.executeTextCommand("paths.get"))

        # Windows
        if platform == "win32":
            code_path = pathlib.Path(PATHS_DICT.get("appDirectory"))

        # Mac OS note that the path is different and requires an additional "Fusion" folder
        elif platform == "darwin":
            code_path = pathlib.Path(PATHS_DICT.get("appDirectory"))

        # Get paths for Design, Mesh, and Flat Pattern tabtoolbar.xml and tabtoolbar.zip

        # Design Toolbar

        # set the path to the Fusion design tabtoolbar.xml on windows
        tb_path = os.path.join(
            code_path,
            "Fusion",
            "Fusion",
            "UI",
            "FusionUI",
            "Resources",
            "Toolbar",
            "TabToolbars.xml",
        )

        # set the path for the Fusion design tabtoolbar.zip archive on windows
        tb_zip = os.path.join(
            code_path,
            "Fusion",
            "Fusion",
            "UI",
            "FusionUI",
            "Resources",
            "Toolbar",
            "TabToolbars.zip",
        )

        # Mesh Toolbar

        # set the path to the Fusion mesh tabtoolbar.xml on windows
        pmtb_path = os.path.join(
            code_path,
            "ParaMesh",
            "UI",
            "ParaMeshUI",
            "Resources",
            "Toolbar",
            "TabToolbars.xml",
        )

        # set the path for the Fusion mesh tabtoolbar.zip archive on windows
        pmtb_zip = os.path.join(
            code_path,
            "ParaMesh",
            "UI",
            "ParaMeshUI",
            "Resources",
            "Toolbar",
            "TabToolbars.zip",
        )

        # Flatpattern Toolbar

        # set the path to the Fusion flatpattern tabtoolbar.xml on windows
        fptb_path = os.path.join(
            code_path,
            "Fusion",
            "Fusion",
            "UI",
            "FusionSheetMetalUI",
            "Resources",
            "Toolbar",
            "TabToolbars.xml",
        )

        # set the path for the Fusion flatpattern tabtoolbar.zip archive on windows
        fptb_zip = os.path.join(
            code_path,
            "Fusion",
            "Fusion",
            "UI",
            "FusionSheetMetalUI",
            "Resources",
            "Toolbar",
            "TabToolbars.zip",
        )

        pathsDict = {
            "Design": [tb_path, tb_zip, tbURL],
            "Mesh": [pmtb_path, pmtb_zip, pmURL],
            "Flatpattern": [fptb_path, fptb_zip, fpURL],
        }

        # Check if the tabtoolbar.xml is there and zip it. This overwrites any existing zip.
        for key, value in pathsDict.items():
            if os.path.exists(value[0]):
                zipfile.ZipFile(value[1], mode="w").write(value[0])
                app.log("Backup of {} tabtoolbar.xml created".format(key))
                urllib.request.urlretrieve(
                    value[2],
                    value[0],
                )
                app.log("Download of new {} tabtoolbar.xml succeeded".format(key))
                next
            else:
                return

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))
