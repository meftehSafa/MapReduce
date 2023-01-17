from multiprocessing import Pool
import os

def map_function(file_name):
    """
    Reads a file and returns a list of tuples, where each tuple contains a word and the number of occurrences of that word
    """
    with open(file_name, 'r') as f:
        # Read the contents of the file
        contents = f.read()
        # Split the contents into words
        words = contents.split()
        # Create a dictionary to store the count of each word
        word_counts = {}
        # Iterate over the words and update the count for each word
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        # Return a list of tuples containing the word and its count
        return [(word, count) for word, count in word_counts.items()]

def reduce_function(word_counts):
    """
    Takes a list of tuples (word, count) and returns a single tuple (word, total_count)
    """
    # Create a dictionary to store the total count of each word
    total_counts = {}
    # Iterate over the list of tuples and update the total count for each word
    for word, count in word_counts:
        if word in total_counts:
            total_counts[word] += count
        else:
            total_counts[word] = count
    # Return a list of tuples containing the word and its total count
    return [(word, count) for word, count in total_counts.items()]

def main():
    # List of file names
    file_list = ["file1.txt", "file2.txt", "file3.txt"]
    # Create a pool of worker processes
    with Pool(processes=len(file_list)) as pool:
        # Apply the map function to each file in the list
        word_counts = pool.map(map_function, file_list)
        # Flatten the list of lists into a single list
        word_counts = [count for sublist in word_counts for count in sublist]
        # Apply the reduce function to the list of tuples
        total_counts = reduce_function(word_counts)
        # Print the results
        for word, count in total_counts:
            print("{}: {}".format(word, count))

if __name__ == "__main__":
    main()
