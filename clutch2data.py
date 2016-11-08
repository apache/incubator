import pickle
import pprint

'''
'clutch2data' reads the pickle file which was created by 'clutch' and generates
various output data files.
'''

inputFile = open('clutch.pkl', 'rb')
projects = pickle.load(inputFile)
inputFile.close()
pprint.pprint(projects)
