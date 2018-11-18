// import nodejs bindings to native tensorflow,
// not required, but will speed up things drastically (python required)
import { canvas, faceapi, faceDetectionNet, faceDetectionOptions, saveFile } from './commons';

import * as fs from 'fs';
import * as path from 'path';
import { LabeledFaceDescriptors, extractFaces } from 'face-api.js';

const IMAGES_FOLDER = './images';


async function getMatcher(): Promise<faceapi.FaceMatcher> {

    await faceapi.nets.ssdMobilenetv1.loadFromDisk('./weights');
    await faceapi.nets.faceLandmark68Net.loadFromDisk('./weights');
    await faceapi.nets.faceRecognitionNet.loadFromDisk('./weights');

    const persons = await new Promise<string[]>((resolve, reject) => {
        fs.readdir(IMAGES_FOLDER, {withFileTypes: true }, (err, folders: fs.Dirent[]) => {
            if (err) {
                return reject(err);
            }
    
            const approvedPersons = ['voislav', 'katerina'];
    
            resolve(
                folders
                .filter((f) => f.isDirectory() && approvedPersons.indexOf(f.name) > -1)
                .map(f => f.name));
        })
    })

    const allPersonsDescriptors = await Promise.all(
        persons.map(async (personName) => {
            const descriptors = await getAllDescriptors(personName);
            return new LabeledFaceDescriptors(personName, descriptors);
        }));
    
    // TODO figure out a way to cache these descriptors for all the images we previously processed
    const matcher = new faceapi.FaceMatcher(allPersonsDescriptors);

    // TODO can be extended to add new persons and their face descriptors to the matcher at runtime
    // new faceapi.FaceMatcher(matcher.labeledDescriptors.concat([new LabeledFaceDescriptors('', null)]));

    return matcher;
}

async function getAllDescriptors(personName: string): Promise<Float32Array[]> {
    
    const personFolder = path.join(IMAGES_FOLDER, personName);

    const personImages = await new Promise<string[]>((resolve, reject) => {
        fs.readdir(personFolder, {withFileTypes: true}, async (err: any, personImageNames: fs.Dirent[]) => {
            if (err) {
                return reject(err);
            }

            resolve(personImageNames.filter((pImage: fs.Dirent) => pImage.isFile()).map(f => f.name));
        })
    });

    const personDescriptors = await Promise.all(
        personImages.map((image) => getFaceDescriptor(personFolder, image))
        );

    return personDescriptors.filter((desc) => !!desc) as Float32Array[];
}

async function getFaceDescriptor(folder: string, imagePath: string): Promise<Float32Array | null> {
    console.log('trying image: ', path.join(folder, imagePath));
    
    const image = await canvas.loadImage(path.join(folder, imagePath));

    const detections = await faceapi.nets.ssdMobilenetv1.locateFaces(image, faceDetectionOptions);
    console.log('detections on image', imagePath, detections);
    const faces = await extractFaces(image, detections);
    if (!faces || faces.length === 0) {
        return null;
    }
    console.log('extracted faces', imagePath, faces);
    const descriptor = await faceapi.nets.faceRecognitionNet.computeFaceDescriptor(faces[0]) as Float32Array;

    return descriptor;
}

async function run() {
    const start = new Date();

    const matcher = await getMatcher();

    const QUERY_IMAGE = './images/voislav4.jpg';
    const queryImage = await canvas.loadImage(QUERY_IMAGE);

    console.log('trying to match image', QUERY_IMAGE);
    const queryFaceRes = await faceapi.detectSingleFace(queryImage, faceDetectionOptions)
        .withFaceLandmarks()
        .withFaceDescriptor();
    
    console.log('query image descriptors', queryFaceRes);
    if (queryFaceRes && queryFaceRes.descriptor) {
        const match = await matcher.findBestMatch(queryFaceRes.descriptor);
        console.log('found match', match);
    }

    const finish = new Date();

    console.log('processing took ', finish.getTime() - start.getTime(), 'ms');
}


run()
    .catch(err => {
        console.error(err);
        process.exit(1);
    })
