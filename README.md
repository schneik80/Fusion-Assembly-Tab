# Fusion360-Assembly-Tab  

## Overview of Changes  

- Introduce a dedicate Assembly Experience
  - Add **Assembly** tab to Fusion design documents
  - New **Assemble** panel in the Assembly tab
    - Moves all Assembly tools to an Assemble panel.
  - New **Motion** panel in the Assembly tab
    - Move motion tools to Motion panel
  - Removes **Assemble** panel from other domain specific ( i.e. Sheetmetal, Plastic, others ) Modeling tabs.
  - Moves **As Built Joint** and **Joint Origin** into an **Advanced** sub menu
  - Removes **Align** from all menus except the Solid tab Modify Panel
  - Joint Origin command is now also in the Construct panel menu across all tabs
- Adds a **PCB** Tab for creation for 3D PCB boards in context of design
- Reorder the **Manage** tab
  - Manage Tab is now before the Utilities tab
  - BOM panel moved to the start of the manage tab tools
- Remove Automated modeling panel
  - **Automated modeling** now appears in Solid Tab's Create panel menu
- Insert Panel cleanup
    -remove asssembly related isnert commands from non-assembly insert panel
- Make the mesh and flatpattern toolbars concistent with general design

### Screenshot

![Assembly  tab preview](./assets/asm-tab.png)

## How to install  with script

Download the tabtoolbar folder and place in your Fusion scripts folder.

Launch Fusion and open the **Scripts and Add-ins manager** on the Utilities tab of a design document.

Run the "TabToolbar" script and follow prompts.


