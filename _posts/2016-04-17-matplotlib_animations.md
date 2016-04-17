---
layout: posts
title: Matplotlib Animations
date: 2016-04-17
---


Sometimes it's pretty cool to have an animated time series in your presentation. I typically make my plots with python's matplotlib, so thankfully if you have ffmpeg installed, this is a fairly straightforward task.

First, you'll need to import matplotlib's animation module

{% highlight python %}
import matplotlib.pyplot as plt
from matplotlib import animation
{% endhighlight %}

Then, setup your figure (here there are two subplots of different sizes)
{% highlight python %}
f,ax = plt.subplots(1,2,gridspec_kw={'width_ratios':[1.5,1]},figsize=(7,3))
l = ax[0].plot(x,y)
{% endhighlight %}

Then initialize the subplots with labels, etc. To animate you'll want an initialization function, and an animation function. The first will setup the plot in the first frame; the latter will take a frame number as an argument and update the plot accordingly.

{% highlight python %}
def init(x,y,l):
	l.set_ydata(y[:1000])
	plt.draw()
	return [l]

def animate(x,y,l,j):
	y = np.roll(y,-2)
	l.set_ydata(y:[1000])
	plt.draw()
	return [l]
{% endhighlight %}

Then you'll want to make the animation, and save the output as a movie

{% highlight python %}
anim = animation.FuncAnimation(f,lambda j: animate(x,y,l,j), init_func= lambda : init(x,y,l), frames = 1000, interval = 1, blit = True)
anim.save('filename.mp4',fps=100,extra_args=['-vcodec','h264','-pix_fmt','yuv420p','-crf','23'])
plt.show()
{% endhighlight %}

Then run the script, and you should have your movie for embedding in a presentation!