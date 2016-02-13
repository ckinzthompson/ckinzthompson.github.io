---
layout: posts
title: Microscope Guide
date: 2016-02-12 
---

---
Make sure you've been trained on microscope use, and how to disconnect the camera.

### Setup

1. Plug in power bricks for:
	1. EMCCD
	2. Green laser power supply
	3. Water circulator


2. Turn on power switches for:
	1. EMCCD
	2. Water circulator
	3. (optional) Red laser -- wait 1 min to turn key
	4. (optional) Blue laser -- wait 1 min to turn key
	5. Shutter controller


3. Turn on the Green Laser: 
	1. Open the PuTTYtel program
	2. Connect to the LASER preset option
	3. Type "on" (don't type the quotes), and hit enter
	4. Type "power=100", and hit enter -- tune power with neutral density filters, not here.
	5. The laser must warm up a few minutes before it will emit light


4. Setup Micro-Manager
	1. Open Micro-Manager
	2. Load preset hardware configuration ("Default\_Camera\_Setting")
	3. Initialize Camera preset to "Regular"
	4. Pick Shutter preset (e.g., "Green") for your desired illumination
	
5. Setup Microscope
	1. Clean both sides of slide with acetone
	2. Clean prism with acetone
	3. Place water on objective
	4. Lower objective, and put slide on microscope stage
	5. Place thin layer of oil on prism, and secure prism to post.
	
6. Image
	1. Find TIRF through eyepiece
	2. Switch to camera, and focus with "Live" mode in Micro-Manager
		1. Adjust histogram limits and bit-depth in Micro-Manager
		2. Focus!
		3. Close shutters by setting Shutters preset to "Off"
		4. Jog platform to new field of view
	3. Setup Acquisition (Standard FRET)
		1. Click "Multi-D Acquisition" in Micro-Manager
		2. Set number of frames (e.g., 1200)
		3. Set interval for frames (e.g., 50)
		4. Set "Channels -> Configuration" to illumination color (e.g., green)
		5. Set "Channels -> Exposure" to the frame interval
	4. Click "Acquire"

7. Cleanup
	1. Lower objective
	2. Remove prism and clean with acetone -- store in box
	3. Remove slide and clean with acetone
	4. Close Micro-Manager
	5. Shutdown green laser by typing "off" in PuTTYtel, and hit enter
	6. Turn off EMCCD (toggle button), water circulator (switch), Red and Blue lasers (key and switch), and 
	7. Unplug power blocks for EMCCD, green laser power supply, and water circulator
	8. Fill out log book with name, hours, power settings, and status
