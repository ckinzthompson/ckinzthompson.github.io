---
layout: posts
title: VMD Rendering
date: 2016-02-18
---

Since Schrodinger acquired Pymol, I've mostly switched to using VMD to render pictures of proteins and other molecules.
I think that it makes nicer looking pictures, with the only downside being alignment is more difficult (maybe I'll talk about this in another post).
I guess that another downside is that it can be very difficult to overcome to learning curve to make really nice looking pictures with VMD.

Here's a short writeup of my VMD settings, though you'll probably have to tweak them.

In Graphics->Representations, I like to draw molecules using:

*Material: AOChalky
*Drawing Method: NewCartoon or NewRibbon
*Color Method: ColorID

For pictures of the ribosome, color the 50S color 15-Ice Blue, and color the 30S a custom tan color.
To do that, set the color to Tan (or something else), then go to Graphics->Colors, and change Tan (or whatever color your chose) to Red 0.99, Green 0.85, Blue 0.71.

To setup a nice view, I like to use Display-> Lights 1 and 2, and Display->Render Mode->GLSL. Though GLSL seems just to deal with the display and not with the rendered pictures -- it's important for seeing what the materials look like though.
Additionally, you can use Extensions->Visualization->Clipping Plane Tool on each molecule that you've loaded (it works on the top molecule (to change top, double click on a different molecule in the 'main' window... you should see the 'T' move)). This will allow you see the interior of molecules a little better. One tip is to remove chains of interest to new pdb files and load them in as separate molecules so that the chain of interest won't be clipped.



Finally, in order to render nice looking pictures, you'll need to do some ray tracing. Before doing that, you should setup Shadows and Ambient Occlusion through Display->Display Settings. Set:

*Shadows: On
*Amb Occl: On
*AO Ambient: 0.8
*AO Direct: 0.3

In order to do the ray tracing, go to File->Render. Here, switch to 'Tacyhon', and pick a new filename for the file (it usually comes out as a TARGA .tga file). Then, in the Render Command before the '-o %s.tga' option, add '-max_surfaces 1 -res 4000 3000'. This will render a very large picture, and most likely it'll take a very long time... but it'll look really nice.

