import os
import glob
from dataclasses import dataclass

@dataclass
class DeployArguments:
    def __init__(
        self,
        pretrained_model_name=None,
        downstream_model_name=None,
        downstream_model_path=None,
    ):
        self.pretrained_model_name = pretrained_model_name
        self.downstream_model_name = downstream_model_name
        self.downstream_model_path = downstream_model_path

        if downstream_model_path is None:
            raise Exception("The path downstream_model_path is required to find the downstream model.")
        else:
            checkpoint_files = sorted(glob.glob("./*.ckpt"), key=os.path.getmtime) # Sort by last modified time
            if len(checkpoint_files):
                raise Exception(f"downstream_model_path \"{downstream_model_path}\" is not valid.")
            
            self.downstream_model_path = checkpoint_files[-1]
            print(f"downstream_model_path: {self.downstream_model_path}")
