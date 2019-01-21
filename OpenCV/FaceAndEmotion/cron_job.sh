clear

echo "The scripts starts at" $(date +'%Y-%m-%d %H:%M')

echo "Setup virtual environment"
virtualenv faceAndEmotion
source faceAndEmotion/bin/activate
#pip install -r requirements.txt

echo "Train model"
python extract_embeddings.py --dataset /mnt/ITLabsEmployeesPictures --embeddings output/embeddings.pickle
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle

echo "Restart Face Recognition application"
kill -9 `pgrep recognize`
python recognize_face_emotion.py --recognizer output/recognizer.pickle --le output/le.pickle &

echo "Deactivate virtual environment"
deactivate

echo "Job done."