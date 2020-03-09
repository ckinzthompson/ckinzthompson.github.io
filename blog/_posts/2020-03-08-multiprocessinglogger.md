---
layout: posts
author: Colin Kinz-Thompson
title: Log progress while using multiprocessing
date: 2020-03-08
---

# Processing a lot of data, and want to keep track of it?

If you're going to process a lot of data in parallel with python, you might want to run code remotely, and track the progress. For instance, I'm running separate, independent calculations on a bunch of files, and I estimate that it will take about one week to finish. Running the following command will execute the code while allowing you to log off, and it won't stop.

``` bash
nohup python -u processing_code.py &
```

The logging/multiprocessing approach in the GIST below will log out the relevant information into a text file called 'log.log'.

{% gist df4c3313c488f08d881d3aa188d963b %}
