import acoustid
import chromaprint
from fuzzywuzzy import fuzz
import numpy as np
import matplotlib.pyplot as plt

duration, fp_encoded = acoustid.fingerprint_file('/home/fsociety/Documents/Pythakon/recordedSou2.wav')
fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)


duration2, fp_encoded2 = acoustid.fingerprint_file('/home/fsociety/Documents/Pythakon/recordedSou1.wav')
fingerprint2, version2 = chromaprint.decode_fingerprint(fp_encoded2)

duration1, fp_encoded1 = acoustid.fingerprint_file('/home/fsociety/Documents/Pythakon/Abel.wav')
fingerprint1, version1 = chromaprint.decode_fingerprint(fp_encoded1)



similarity = fuzz.ratio(fingerprint1, fingerprint)
print(similarity)

similarity = fuzz.ratio(fingerprint2, fingerprint)
print(similarity)

similarity = fuzz.ratio(fingerprint1, fingerprint2)
print(similarity)