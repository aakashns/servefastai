# servefastai

Serve FastAI models and get a web-based UI to test them out with a single line of code.

![screenshot](https://i.imgur.com/TzZQZUs.jpg)

## Installation

Install with `pip`. Make sure you have `fastai` already installed.

```
pip install servefastai
```

## Usage

```
from servefastai import serve
serve(learn)
```

`learn` should be a FastAI learner object. Navigate to http://PUBLIC_IP:9999 , where `PUBLIC_IP` is the public IP address of the machine running the Jupyter notebook. You will see a form where you can upload one or more images. Upload the images and click submit to view the predictions.
