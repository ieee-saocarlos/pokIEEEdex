# Quick example

## Install dependencies
`git clone https://github.com/ieee-saocarlos/pokIEEEdex`
`pip install requirements`

## Load indices dict
```
with open(./"indices.json", "r") as f:
    indices = eval(f.read())
```

## Make predicts
```
from models import loli_model2

image_path = ... # write the path to the pokemon image

pred_index = loli_model2.predict(image_path)
pokemon_name = indices[pred_index]
print(pokemon_name)
```