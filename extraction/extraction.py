from pyAudioAnalysis import audioBasicIO
 from pyAudioAnalysis import audioFeatureExtraction
 import os
 import json

 labels = []
 features = []
 
 datadir = "../S-1A/audio/aligned/"
 for filename in os.listdir(datadir):
 	if "lie" in filename:
 		labels.append(1)
 	else:
 		labels.append(0)
 	[Fs, x] = audioBasicIO.readAudioFile(datadir+filename)
 	
 	st_features = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
 	features.append(st_features.tolist())

 with open('labels.json', 'w') as label_file:
 	json.dump(labels,label_file)
 with open('extracted_features.json','w') as feature_file:
 	json.dump(features,feature_file)
