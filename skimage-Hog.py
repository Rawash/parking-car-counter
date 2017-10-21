
import glob
import numpy as np 
from skimage.feature import hog
from sklearn.preprocessing import StandardScaler
from skimage import color, exposure, io

# from dataHandling import dataBase 

# Positive, Negative = dataBase() 
 
# def extract_feature(images):
#     features = np.array([])
#     for image in images:
#         sourceImage = color.rgb2gray( io.imread(image) )
#         hog_features = hog(sourceImage, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualise=False, feature_vector=True) 
#         features = np.append(features,hog_features)
#         print(hog_features.ndim)
        
#         print(image)
         
#     return features

# car_features = extract_feature(Positive)
# car_features.dump("car_features_RGB.dat")

# notcar_features = extract_feature(Negative)
# notcar_features.dump("notcar_features_RGB.dat")

###

car_features = np.load("car_features.p")
print("car_file Loaded" , len(car_features ) )

notcar_features =  np.load("notcar_features.p")
print("notcar_file Loaded ", len(notcar_features) )

# minNump = np.min(np.array([car_features.size, notcar_features.size]))
# print(minNump)
# # car_features = car_features
# print("car_file Loaded" , len(car_features ))
# notcar_features = notcar_features
# print("notcar_file Loaded ", len(notcar_features) )

### 

# Create an array stack of feature vectors
X = np.concatenate( ( car_features, notcar_features ) )
print( 'X.shape', X.shape )

# Fit a per-column scaler 
X_scaler = StandardScaler().fit(X)
# Apply the scaler to X
scaled_X = X_scaler.transform(X)

np.asarray(X_scaler).dump("saved_X_scaler.dat")

# Define the labels vector
y = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))


# Split up data into randomized training and test sets
rand_state = np.random.randint(0, 100)
X_train, X_test, y_train, y_test = train_test_split(scaled_X, y, test_size=0.2, random_state=rand_state)


# Use a linear SVC 
svc = LinearSVC()
svc.fit(X_train, y_train)

svc.dump("saved_svc.dat") 