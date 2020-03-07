---
layout: posts
title: Encoding Movies for Mac with FFMPEG
date: 2016-02-18
---

Here's how to make a movie from a bunch of pictures using FFMPEG that will play on a mac for a presentation
Assuming that you've saved your pictures as inputfile_xxxxx.png, where xxxxx is a number prefaced with leading zeros, use
{% highlight bash %}
ffmpeg -i inputfile_%05d.png -c:v libx264 -preset veryslow -qp 0 output.mp4
{% endhighlight %}

Unfortunately, you probably will need to make sure that it can play in a presentation, so you need to play some encoding tricks.
I think that easiest way is to use Handbrake, however you can also take the movie and convert it using ffmpeg by

{% highlight bash %}
ffmpeg -i input.mp4 -vcodec libx264 -crf 0 -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -r 25 output.mp4
{% endhighlight %}