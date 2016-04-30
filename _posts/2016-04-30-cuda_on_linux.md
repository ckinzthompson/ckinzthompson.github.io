---
layout: posts
title: Getting CUDA set up on Linux
date: 2016-04-30
---


CUDA [[https://en.wikipedia.org/wiki/CUDA]] is an approach to programming NVIDIA graphic processing units (GPUs) in order to accelerate computations [[https://developer.nvidia.com/cuda-zone]]. This is really advantageous because of the number of simultaneous calculations that can be performed on a GPU due to the presence of many many many 'cores'. It's unfortunately, kind of difficult to get setup on a Linux computer. I spent a while messing up my own computer to do so; so, here are some notes about how to do this without messing up your computer (or how to fix it if you do).

First, you'll need a CUDA competent NVIDIA GPU. Check this list on wikipedia to make sure that your GPU can handle CUDA: [[https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units]]. Then you'll need to make sure that you have the proper proprietary drivers for the GPU from NVIDIA. Use this NVIDIA site, [[http://www.nvidia.com/Download/index.aspx?lang=en-us]], to download find out which driver version you should be using. Then, if you're using ubuntu (I'm using xubuntu for this), you can just download the proper version using apt-get.
For instance, I'm using a Geforce GTX 750 Ti, and that needed the 361 version of the driver. You can get that version from by issuing the following command in a terminal:

{% highlight console %}
sudo apt-get install nvidia-361
{% endhighlight %} 

You'll also probably want to restart your computer at this point. If something goes wrong, you'll want to google how to switch back from NVIDIA drivers to the original, generic, linux drivers called 'Nouveau'. Okay, now you'll have to start to install the CUDA toolkit -- there are a couple of different version (current is 7.5 or 8?), but you need to use the one that works for your driver version. Some googling, and you should find that. I used version 7.5 of the toolkit. Anyway... time to install! Go to the CUDA toolkit downloads site [[https://developer.nvidia.com/cuda-downloads]], and select Linux, x86\_64, Ubuntu, 15.04, and runfile (local) -- this will download a ~1 gb file for the installer. 

Okay before installing, there's some funny business. You'll need to kill your Xserver for the install, and then bring it back after. X is what provides the graphics on your machine... so this means no GUI for anything. It's helpful to have a second computer around in case anything goes wrong and you need to google answers from stackoverflow.

OKAY - You'll need to need to enter a TTY session (control+alt+f1) and do everything from here. To go back to the GUI, you can press (control+alt+f7). Login to the TTY session, then, to stop the Xserver, issue the command 

{% highlight console %}
sudo service lightdm stop
{% endhighlight %}

(you shouldn't see anything if you press (control+alt+f7)... make sure to go back to the TTY session if you do this (control+alt+f1)). Navigate to your Downloads folder, and run installer. You might want to change the permissions first with 

{% highlight console %}
chmod 755 installer_filename.run
./installer_filename.run
{% endhighlight %}

This will prompt you for various install options. SKIP THE DRIVER INSTALLATION. Install the toolkit as root, and also the samples. Once this is done, you'll want to boot the X server back up using 

{% highlight console %}
sudo service lightdm start
{% endhighlight %}

Assuming everything installed successfully, you probably still need to do some fun fixes. For instance, you can't actually run the CUDA compiler with the latest version of gcc and g++ (which it needs), so you'll have to provide it with the older ones. To do so, try

{% highlight console %}
sudo apt-get install gcc-4.7 g++-4.7
sudo ln -s /usr/bin/gcc-4.7 /usr/local/cuda-7.5/bin/gcc
sudo ln -s /usr/bin/g++-4.7 /usr/local/cuda-7.5/bin/g++
{% endhighlight %}

this will have created symbolic links for CUDA to the older versions. Finally, in you'll also need to add the cuda bin and libraries to your path. If you're using zsh add the following to ~/.zshrc

{% highlight console %}
export CUDA_HOME="/usr/local/cuda-7.5"
export PATH="${CUDA_HOME}/bin:$PATH"
export LD_LIBRARY_PATH="${CUDA_HOME}/lib64:$LD_LIBRARY_PATH"
{% endhighlight %}

And then save that, and source it with 
{% highlight console %}
source ~/.zshrc
{% endhighlight %}

This should have CUDA set up. In order to check that it worked, go to the samples that it installed (in your home folder by default). Enter the 1\_Utilities folder and then the deviceQuery folder. Make this program, and then run it using

{% highlight console %}
make
./deviceQuery
{% endhighlight %}

You should see output that says it passed. If so, congratulations!
