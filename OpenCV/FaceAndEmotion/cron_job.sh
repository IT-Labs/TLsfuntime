clear

echo "The scripts starts now."

python extract_embeddings.py --dataset /mnt/ITLabsEmployeesPictures --embeddings output/embeddings.pickle
python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle

echo "Job done."