# Fusion360-Assembly-Tab  

## Overview of Changes  

- Introduce a dedicate Assembly Experience
  - Add **Assembly** tab to Fusion 360 design documents
  - New **Assemble** panel in the Assembly tab
  - Moves all Assembly tools to an Assemble panel.
  - New **Motion** panel in the Assembly tab
  - Move motion tools to Motion panel
  - Removes **Assemble** panel from other domain specific ( i.e. Sheetmetal, Plastic, others ) Modeling tabs.
    > NOTE: To remove Assemble from the Mesh tab requires an additional xml document to be modified.
  - Moves **As Built Joint** and **Joint Origin** into an **Advanced** sub menu
  - Removes **Align** from all menus except the Solid tab Modify Panel
  - Joint Origin command is now also in the Construct panel menu across all tabs
- Adds a **PCB** Tab for creation for 3D PCB boards in context of design
- Reorder the **Manage** tab
  - Manage Tab is now before the Utilities tab
  - BOM panel moved to the start of the manage tab tools
- Remove Automated modeling panel
  - **Automated modeling** now appears in Solid Tab's Create panel menu

### Screenshot

![Assembly  tab preview](./assets/asm-tab.png)

## How to install  with script

Download the tabtoolbar folder and place in your fusion scripts folder.

Launch Fusion and open the Scripts and Add-ins manager on the Utilities tab of a design document.

Run the "TabToolbar" script and follow prompts.


## Hown to install manualy

**!!! Backup your original TabToolbar.xml before using this new toolbar definition xml !!!**

Download the ()[Tabtoolbar.xml]

On **Mac OS**, over-write the existing file here:

    /Users/ <Your User Name> /Library/Application Support/Autodesk/webdeploy/production/ <Current deployment GUID> /Autodesk Fusion 360.app/Contents/Libraries/Applications/Fusion/Fusion/UI/FusionUI/Resources/Toolbar/TabToolbars.xml`

On **Windows**, over-write the existing file here:

    \Users\ <Your User Name> \AppData\Local\Autodesk\webdeploy\production\ <Current deployment GUID> \Fusion\UI\FusionUI\Resources\Toolbar\TabToolbars.xml

Relaunch Fusion 360.

## Uninstall

To uninstall, restore the original file you archived and restart Fusion 360.

## Special instructions for Mesh tab

To remove Assemble tools from Mesh Tab toolbar:

**!!! Backup your original TabToolbar.xml before modifying !!!**

On **Mac OS**, edit the existing file here:

> /Users/ <Your User Name> /Library/Application Support/Autodesk/webdeploy/production/ <Current deployment GUID> /Autodesk Fusion 360.app/Contents/Libraries/Applications/Paramesh//UI/ParaMeshUI/Resources/Toolbar/TabToolbars.xml`

On **Windows**, edit the existing file here:

> \Users\ <Your User Name> \AppData\Local\Autodesk\webdeploy\production\ <Current deployment GUID> \ParaMesh\UI\ParaMeshUI\Resources\Toolbar\TabToolbars.xml

From `Tab Id="ParaMeshOuterTab"`  

Remove `"AssemblePanel;"`  

So the line now reads: `"Panels="ParaMeshCreatePanel;ParaMeshPreparePanel;ParaMeshModifyPanel;ConfigurePanel;ConstructionPanel;InspectPanel;InsertPanel;ParaMeshSelectPanel;ParaMeshExportPanel;SnapshotPanel"`

From `Tab Id="ParaMeshBaseFeatureTab"`  

Remove `"AssemblePanel;"`  

So the line now reads: `Panels="ParaMeshCreateBaseFeature;ParaMeshPreparePanel;ParaMeshModifyPanel;ConstructionPanel;InspectPanel;ParaMeshSelectPanel;ParaMeshExportPanel;ParaMeshBaseFeatureStopPanel"`
