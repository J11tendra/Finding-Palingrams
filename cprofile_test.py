#Importing the cProfile library to get the statistics of the processing and the code file to be analyzed:
import cProfile, find_palingrams

#Calling the Function:
cProfile.run('find_palingrams.find_palingrams()')
