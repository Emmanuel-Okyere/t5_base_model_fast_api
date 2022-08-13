# T5-base Model and Fast API

# What is the t5 base model
The model t5 base is a Natural Language Processing (NLP) Model implemented in Transformer library, generally using the Python programming language used for text-text translations.

For more information about the model, visit https://huggingface.co/t5-base

# Installation
Fork the project at https://github.com/Emmanuel-Okyere/shoppharma.git
```sh
  ├── README.md
  ├── pyproject.toml *** the package manager. 
  ├── poetry.lock *** poetry
  ├── Dockerfile *** Docker file
  ├── pyproject *** main application folder
        ├── api
        │   ├── translation.py
        |   schemes
        |   ├── translation.py 
        |   core
        |   ├── config.py ***setting for the application
        └── main.py *** driver for the application
  
  ```
Building with Docker in the forked directory
```

docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage

```
Building with Poetry in the forked directory
```
pip install poetry
poetry intall
unicorn pyproject.main:app
```

Navigate to http://127.0.0.1:8000/

**Note** On startup, the t5-base model would be downloaded.

The application was developed with a 24GB RAM and 1.80GHz CPU Speed.

## Visuals
![Home Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/English%20-%20German.png?raw=true)
![Home Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/English%20to%20French.png?raw=true)
![Home Page](https://github.com/Emmanuel-Okyere/readme_images/blob/main/ShopPharma/English%20to%20Romania.png?raw=true)