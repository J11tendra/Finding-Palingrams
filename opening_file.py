#Function to open a file:
def open_file(file_path):
	'''Opening a file; forming a List of lowercase words.'''
	try:	
	    with open(file_path,'r') as file:
	    	word_list = file.read().lower().strip().split('\n')

	    return word_list
    
	except OSError as er:
		print(f'{er} Error Opening {file_path}. Terminating Program.')

#Defining a file path:
file_path = 'Enter the file path here'
