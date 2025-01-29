import adsk.core, adsk.fusion, adsk.cam, os, sys, traceback, pathlib, zipfile, json
import urllib.request
from sys import platform

# import adsk.cam

# Initialize the global variables for the Application and UserInterface objects.
app = adsk.core.Application.get()
ui = app.userInterface
url = "https://raw.githubusercontent.com/schneik80/Fusion-Assembly-Tab/main/TabToolbars.xml"  # URL to the main branch in GITHUB for the new tabtoolbar.xml


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
        # Windows
        if platform == "win32":
            winassytb()

        # Mac OS
        elif platform == "darwin":
            macassytb()

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
def winassytb():
    try:
        PATHS_DICT = json.loads(app.executeTextCommand("paths.get"))
        code_path = pathlib.Path(PATHS_DICT.get("appDirectory"))

        # set the path to the tabtoolbar.xml
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

        # set the path for the tabtoolbar.zip arrchive
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

        # Check if the tabtoolbar.xml is there and zip it. This overwrites any existing zip.
        if os.path.exists(tb_path):
            zipfile.ZipFile(tb_zip, mode="w").write(tb_path)
        else:
            return

        # Get the tabtoolbar.xml from the URL
        urllib.request.urlretrieve(
            url,
            tb_path,
        )

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))


# Mac OS
def macassytb():
    try:
        PATHS_DICT = json.loads(app.executeTextCommand("paths.get"))
        code_path = pathlib.Path(PATHS_DICT.get("appDirectory"))

        # set the path to the tabtoolbar.xml
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

        # set the path for the tabtoolbar.zip archive
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

        # Check if the tabtoolbar.xml is there and zip it. This overwrites any existing zip.
        if os.path.exists(tb_path):
            zipfile.ZipFile(tb_zip, mode="w").write(tb_path)
        else:
            return

        # Get the tabtoolbar.xml from the URL
        urllib.request.urlretrieve(
            url,
            tb_path,
        )

    except:
        if ui:
            ui.messageBox("Failed:\n{}".format(traceback.format_exc()))
