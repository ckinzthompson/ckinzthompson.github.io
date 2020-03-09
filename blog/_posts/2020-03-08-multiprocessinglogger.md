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

``` python
import multiprocessing
import logging
import numpy as np

logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s %(process)s %(levelname)s %(message)s',
	filename='log.log',
	filemode='w'
)
import logging.config
logging.config.dictConfig({
	'version': 1,
	'disable_existing_loggers': True,
})

#################

def process_data(theta):
	job_name, job_ind, job_total, otherparameters = theta

	## Start Logging
	with multiprocessing.Lock():
		logging.debug("Started  %s.  %2.1f%%"%(pdb_id,100*float(job_ind+1)/float(job_total)))
	t0 = time.time()

	## Main processing
	try:
		for i in range(100000):
			a = i + 1
	except: ## catch an error
		with multiprocessing.Lock():
			logging.debug('ERROR: issue with %s'%(job_name))
		return None

	## Stop Logging
	t1 = time.time()
	with multiprocessing.Lock():
		logging.debug("Finished %s.  %.6f sec"%(job_id,t1-t0))

	return None

if __name__ == '__main__':
	logging.debug("Processing Started")

	## input parameters - job name, job index, total number of jobs, other paramters
	total = 100
	input_list = [[str(np.random.rand()), i, total, np.random.rand()] for i in range(total)]

	with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
		pool.map(process_data, input_list)

	logging.debug("Processing completed")
```
