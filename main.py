""" With the fiftyone library enable exploration of the open-images-v7 dataset"""


import fiftyone
import fiftyone as fo
import fiftyone.zoo as foz

dataset = fiftyone.zoo.load_zoo_dataset(
              "open-images-v7",
              split="train",  # Pictures meant for training model
              label_types=["detections", "segmentations", "points"],
              classes=["Owl", "Sheep"],  # Classes for animals
              max_samples=500,  # Quantity of dataset in pictures ex. 500 pictures
          )
session = fo.launch_app(dataset, port=5151)  # Create localhost session to explore dataset
session.wait()  # Prevent termination of localhost until quit
