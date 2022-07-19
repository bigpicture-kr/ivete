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
        inference_args=None,
    ):
        self.pretrained_model_name = pretrained_model_name
        self.downstream_model_name = downstream_model_name
        self.downstream_model_path = downstream_model_path
        self.inference_args = inference_args

        if downstream_model_path is None:
            raise Exception("The path downstream_model_path is required to find the downstream model.")
        else:
            checkpoint_files = glob.glob(os.path.join(downstream_model_path, "*.ckpt"))
            checkpoint_files = sorted(checkpoint_files, key=os.path.getmtime) # Sort by last modified time
            if len(checkpoint_files) == 0:
                raise Exception(f"downstream_model_path \"{downstream_model_path}\" is not valid.")
            
            self.downstream_model_path = checkpoint_files[-1]
            print(f"downstream_model_path: {self.downstream_model_path}")
