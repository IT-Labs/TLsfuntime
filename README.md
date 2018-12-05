# TLsfuntime

## Instructions for OpenCV/Face3 example

- This can't run this under Windows Subsystem for Linux because it doesn't support camera devices at the time of this writing
- This can run on a Ubuntu 64-bit Linux VM, under VirtualBox (make sure VirtualBox Extension Pack is installed and Devices/WebCams/{YourCamera} is checked)

To run this on Linux:

1. open Terminal
2. install python 

```
sudo apt install python
```

3. install pip - python package manager

```
sudo apt install python-pip
```

4. install virtualenv - a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

```
sudo apt install virtualenv
```

5. install git, clone the project into your desired location and navigate to OpenCV/Face3 example

```
sudo apt install git
git clone  https://github.com/IT-Labs/TLsfuntime.git
cd TLsfuntime
cd OpenCV
cd Face3
```

6. create a python virtual environment for this project and start using it

```
virtualenv face3
source face3/bin/activate
```

7. install the necessary python packages with pip

```
pip install imutils
pip install numpy
pip install opencv-python
pip install scikit-learn
```

8. compute the face embeddings and serialize the data in a pickle file
```
python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7
```

9. train the face recognition model
```
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle
```

10. execute the OpenCV face recognition pipeline on a video stream (from camera with index 0)
```
python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle
```

(11.) to exit the python virtual environment and continue with normal work on the Terminal, you can use

```
deactivate
```


