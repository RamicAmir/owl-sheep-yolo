""" With the fiftyone library enable exploration of the open-images-v7 dataset"""


import fiftyone
import fiftyone as fo
import fiftyone.zoo as foz

dataset = fiftyone.zoo.load_zoo_dataset(
              "open-images-v7",
              split="train",
              label_types=["detections", "segmentations", "points"],
              classes=["Owl", "Sheep"],
              max_samples=500,
          )
session = fo.launch_app(dataset, port=5151)
session.wait()
