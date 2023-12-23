# TF-IDF Calculation

This project was completed as the second homework assignment for the university course "Parallel Programming." The primary objective was to practice utilizing Python's `reduce` and `lambda` functions.

## Overview
The task involves implementing the TF-IDF (term frequency–inverse document frequency) following the Map-Reduce paradigm.

### Tasks
1. **Calculating TF Values from a Single Text**
    - It should return a list of tuples `(file identifier, word, frequency of the word occurrence)`.
    - Calculate word frequency based on the formula: 
        ```
        tf(t, d) = Number of occurrences of word t in document d / Total number of words in document d
        ```

2. **Calculating TF Values from All Texts**
    - Resulting in a single list containing tuples from all files.

3. **Calculating IDF Values**
    - IDF is calculated using the formula: 
        ```
        idf(t) = log(Number of documents in the set / Number of documents where word t appears)
        ```

4. **Calculating TF-IDF Values (4 points)**
    - The result should be in the form of a list of tuples `(word, file identifier, value)`.
    - Sort the list so that all words related to one file appear consecutively, and within each file, by descending TF-IDF values.
