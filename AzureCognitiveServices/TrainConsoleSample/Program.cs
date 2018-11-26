using System;
using VideoFrameAnalyzer;
using Microsoft.ProjectOxford.Face;
using Microsoft.ProjectOxford.Face.Contract;
using System.Threading.Tasks;
using System.IO;
using System.Configuration;

namespace BasicConsoleSample
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            FrameGrabber<Face[]> grabber = new FrameGrabber<Face[]>();

            Task.Run(async () =>
            {
                try
                {
                    var isModelTrained = await TrainModel();

                    if(isModelTrained)
                    {
                        Console.WriteLine("Model has been successfully trained");
                    }
                    else
                    {
                        Console.WriteLine("An error occurred while training model");
                    }
                }
                catch(Exception ex)
                {
                    throw ex;
                }

            });
          
            Console.WriteLine("Press any key to stop...");
            Console.ReadKey();
        }

        private static async Task<bool> TrainModel()
        {
            // Create Face API Client.
            FaceServiceClient faceServiceClient = new FaceServiceClient(
                ConfigurationManager.AppSettings["SubscriptionKey"],
                ConfigurationManager.AppSettings["ApiRoot"]);

            // Create an empty PersonGroup
            string personGroupId = "familija";
            await faceServiceClient.CreatePersonGroupAsync(personGroupId, "Familija");

            //trained by specified image folders
            await TrainPerson(faceServiceClient, "Kosta", personGroupId, @"dataset\Kosta\");
            await TrainPerson(faceServiceClient, "Jasmina", personGroupId, @"dataset\Jasmina\");

            await faceServiceClient.TrainPersonGroupAsync(personGroupId);

            TrainingStatus trainingStatus = null;
            while (true)
            {
                trainingStatus = await faceServiceClient.GetPersonGroupTrainingStatusAsync(personGroupId);

                if (trainingStatus.Status != Status.Running)
                {
                    break;
                }

                await Task.Delay(1000);
            }

            return true;
        }

        private static async Task<bool> TrainPerson(FaceServiceClient faceServiceClient, string name, string personGroupId, string imageDir)
        {
            var person = await faceServiceClient.CreatePersonAsync(
             // Id of the PersonGroup that the person belonged to
             personGroupId,
             // Name of the person
             name
             );

            //todo: store PersonId/Pair in json file that can be later used for face recognition

            // Directory contains image files
            foreach (string imagePath in Directory.GetFiles(imageDir, "*.jpg"))
            {
                using (Stream s = File.OpenRead(imagePath))
                {
                    // Detect faces in the image and add to Anna
                    var addPersonFaceResult = await faceServiceClient.AddPersonFaceAsync(
                        personGroupId, person.PersonId, s);
                }
            }

            return true;
        }
    }
}
