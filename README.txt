Last updated: 2014-05-18


1. Description

	Python exercises on manipulation and simple querying of large csv files. This is a series of exercises to do simple analytical queries over datasets stored in large files. It is also an opportunity to practice different Python-based technologies.

	The intention of this work is to be used as a sandbox for testing different technologies to better understand what is best suited for analytical tasks on similar files. Ideally, the resulting code should be unit tested, documented and simple enough to be part of future more ambitious projects. Also, parallelization should be considered. For simplicity, I will consider Spark (possibly loading files from on hdfs) as the first parallel framework to try because of its native Python support.


2. Technology/dependencies

These exercises will use the following Python-based technologies:

	* "Vanilla" Python 2.7
	* IPython notebooks (with a public viewer using nbviewer.ipython.org)
	* matplotlib
	* Pandas
	* scipy + numpy
	* Json (Python module)
	* a web server (such as cherrypy)
	* unittest
	* PySpark (PoC only)
	* cython (PoC only)

	
3. License

	MIT license http://opensource.org/licenses/mit-license.html
	
	
4. Specification (What is going to be implemented)

	5.1. Must have

	To do
	
		5. Exercises on displaying results as a web service	
	
	Doing

	
	Done

		1. Exercises on line counting, byte counting, reading dates
		2. Exercises on simple aggregation functions and sorting
		3. Exercises on keeping updated dictionary tables for external services (such as GeoBases in Github)
		4. Exercises on joining different files 
	
	
	5.2. Nice to have

	To do
	
		1. Unit testing for all reusable code (Proof of concept only)
		2. Parallelization using PySpark (Proof of concept only)
		3. Cython: Compiling Python as C, integrating C++ function in Python (Proof of concept only)
		
		
	Doing
	Done
