---
layout: post
author: Colin Kinz-Thompson
title: Fixing Java Programs Your Lab-Mate Wrote Ages Ago
date: 2016-03-08
---


We have a java program as a .jar file that my lab uses to do some standard data processing. Unfortunately, it was written quite a long time ago, by someone who is no longer in the lab. New instrumentation has required that we update this software to work with new types of data (e.g., format, size, bit-depth, etc.). As a result, I've had to learn how to edit this java program. To do that:

1) Unpack the .jar file with Archive Manager (Mac) or some other program


2) Modify the .java file(s) with a text editor


3) Compile the edited .java file(s) into .class files with
{% highlight bash %}
javac foo.java
{% endhighlight %}
where foo.java is the file name.


4) Check that your edits work like you want using
{% highlight bash %}
java foo
{% endhighlight %}


5) Pack the files into a new .jar file for distribution
{% highlight bash %}
jar -cfve foo.jar mainclassfile *
{% endhighlight %}
where foo.jar will be the new .jar file name, mainclassfile is the main file without the .class suffix, and the * means to include all the files in the folder.
