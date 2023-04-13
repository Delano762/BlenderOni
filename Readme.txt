# BlenderOni 1.1
# Author: Delano762

## Description
BlenderOni is a Blender addon developed as a companion tool to the Rigify rig for Oni available here with all the relevant documentation: http://mods.oni2.net/node/388

## Installation
1. Unpack BlenderOni.py anywhere on your disk
2. Open Blender
3. Go to Edit / Preferences / Add-ons
4. Click Install
5. Select BlenderOni.py

You should now have a BlenderOni panel available in the side panels of the 3D Viewport.

## Credits

- Geyser - for creating the Rigify-Oni rig and all the help
- EdT, Iritscen - general help with the addon
- Danta - most of the code in the Throw Adjuster script

## 1.1 Changelog:
-Made visual transformers select the given frame 4 times instead of one. If a number of connected objects or bones in Blender are constrained and animated, selecting any frame of the animation will initially cause the bones to position and rotate themselves incorrectly, making the Visual Transformation inaccurate. The solution is to simply select the given frame about 2 to 4 times, which is what this fix does.

## 1.0.1 CL:
-Added Constrain Character Model option