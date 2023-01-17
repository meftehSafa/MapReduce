# parallel MapReduce problem

This program is about creating a local parallel MapReduce program, counting the total number of each word in
different files.

This algorithm uses the "multiprocessing" library to create a pool of worker processes that run in parallel. 

The "map_function" reads the contents of a file, splits it into words, and returns a list of tuples containing each word and the number of occurrences of that word.

The "reduce_function" takes a list of these tuples and returns a single tuple containing each word and the total number of occurrences across all files.

The "main" function applies the "map_function" to each file in a list of file names using the worker pool, then applies the "reduce_function" to the resulting list
