# ivete
End-to-Inference Machine Learning Framework

## Install

```bash
pip install git+https://github.com/bigpicture-kr/ivete.git
```

## Requirements

- Checkpoint file of the trained model
- [PyTorch](https://pypi.org/project/torch/)
- [Tranformers](https://pypi.org/project/transformers/)
- [Flask](https://pypi.org/project/Flask/)
- [Flask-Cors](https://pypi.org/project/Flask-Cors/)

## Usage

### Inference

There are two examples of inferring Q&A tasks through ivete in Jupyter Notebook and Python script.

- in Jupyter Notebook - [examples/qa/qa.ipynb](https://github.com/bigpicture-kr/ivete/blob/main/examples/qa/qa.ipynb)
- in Python script - [examples/qa/qa.py](https://github.com/bigpicture-kr/ivete/blob/main/examples/qa/qa.py)

The steps below are the same as the Q&A examples.

#### Step 1. Train model

Ivete requires a checkpoint file of the trained model to run. It doesn't provide features for model training. Therefore, you need to train model using a different framework.

It is recommended to use the [🧐MiNSU](https://github.com/bigpicture-kr/MiNSU) to train model. But doesn't matter which framework is used to train.

#### Step 2. Import python libraries

Import necessary classes from PyTorch, Transforemrs and ivete.

```python
import torch
from transformers import BertConfig, BertForQuestionAnswering, BertTokenizer
from ivete.deploy import DeployArguments, deploy
```

#### Step 3. Set up deployment arguments

Set arguments for deployment. Each argument is as follows.

- `pretrained_model_name` - The name of the model pretrained using Transformers. The model will be loaded automatically from [Hugging Face](https://huggingface.co).
- `downstream_model_path` - The path where the fine-tuned model is located to perform the downstream task. The latest version of the checkpoint files with .ckpt extension located in that path will be loaded.
- `inference_args` - Other arguments required for model inference. Make it the same as set during train.

```python
args = DeployArguments(
    pretrained_model_name="beomi/kcbert-base",
    downstream_model_path="./checkpoints/",
    inference_args={
        'max_seq_length': 128,
        'max_query_length': 32,
    }
)
```

#### Step 4. Load the model and configurations

Load the configurations of the pretrained model and checkpoints of the fine-tuned model. You can set which device - CPU or GPU to infer with the `map_location` argument.

```python
pretrained_model_config = BertConfig.from_pretrained(
    args.pretrained_model_name
)
tokenizer = BertTokenizer.from_pretrained(
    args.pretrained_model_name,
    do_lower_case=False,
)

checkpoint = torch.load(
    args.downstream_model_path, 
    map_location=torch.device("cpu"),
)

model = BertForQuestionAnswering(pretrained_model_config)
model.load_state_dict({k.replace("model.", ""): v for k, v in checkpoint['state_dict'].items()})
```

#### Step 5. Switch the model into evaluation mode

```python
model.eval()
```

#### Step 6. Implement the inference method

The inference method must be implemented as a single function. Annotations of parameters must be specified as ivete builds the function's parameters as a web tool for inference.

```python
def inference(question: str, context: str):
    # Python script for inference
    return {
        # Output data from the model
        'output': pred_text,
    }
```

For a full example of the inference method, see [examples/qa/qa.py](https://github.com/bigpicture-kr/ivete/blob/main/examples/qa/qa.py#L33).

#### Step 7. Run as web tool for inference

Execute as a web tool with arguments for deployment. The web server runs with Flask. The descriptions of deployment arguments are as follows.

- `inference` - Inference method implemented in the previous step.
- `api_name` - API prefix for web server.
- `template_name` - The name of the web frontend template. The default value is `default`. It has only a simple input and output box in `default` template.
- `template_path` - The path where the web frontend template is located. If it is stored in `templates/{template_name}`, no need to specify this.

```python
app = deploy(
    inference=inference,
    api_name="qa",
)
app.run()
```

If you want to know how ivete's deploy works, take a look at this module - [ivete/deploy/\_\_init\_\_.py](https://github.com/bigpicture-kr/ivete/blob/main/ivete/deploy/__init__.py).

### Build web template

Preparing...
