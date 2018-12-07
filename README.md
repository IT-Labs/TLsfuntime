# TLsfuntime

## Instructions for OpenCV/FaceAndEmotion example
#### this is an example that recognizes faces (from trained ML dataset) and emotions (from pretrained model)

- This can't run this under Windows Subsystem for Linux because it doesn't support camera devices at the time of this writing
- This can run on a Ubuntu 64-bit Linux VM, under VirtualBox (make sure VirtualBox Extension Pack is installed and Devices/WebCams/{YourCamera} is checked)

1. open Terminal
2. install python 

```
sudo apt install python
```

3. install pip - python package manager

```
sudo apt install python-pip
```

4. install virtualenv - a tool to create isolated Python environments. This tool creates a folder which contains all the necessary executables to use the packages that a Python project needs.

```
sudo apt install virtualenv
```

5. install git, clone the project into your desired location and navigate to OpenCV/FaceAndEmotion example

```
sudo apt install git
git clone  https://github.com/IT-Labs/TLsfuntime.git
cd TLsfuntime
cd OpenCV
cd FaceAndEmotion
```

6. create python virtual environment for this project and start using it

```
virtualenv faceAndEmotion
source faceAndEmotion/bin/activate
```

7. install all the necessary python packages within the python virtual environment using the requirements.txt file

```
pip install -r requirements.txt
```

8. compute the face embeddings and serialize the data in a pickle file
```
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle 
```

9. train the face recognition model
```
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle
```

10. execute the OpenCV face recognition pipeline, along with the emotion prediction and probabilities on a video stream (from camera with index 0)
```
python recognize_face_emotion.py --recognizer output/recognizer.pickle --le output/le.pickle
```

(11.) to exit the python virtual environment and continue with normal work on the Terminal

```
deactivate
```


