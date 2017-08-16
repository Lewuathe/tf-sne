tf-sne [![Docker Pulls](https://img.shields.io/docker/pulls/lewuathe/tf-sne.svg)](https://hub.docker.com/r/lewuathe/tf-sne/)
====

[t-SNE](https://lvdmaaten.github.io/tsne/) is a state of the art dimension reduction algorithm and 
there are [several implementations](http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) available.
tf-sne is a light weight visualization tool by using [Tensorflow](http://tensorflow.org/), [Tensorboard](https://www.tensorflow.org/get_started/embedding_viz). tf-sne create a embedding matrix of given data sets and converts 
it into Tensorflow projection format.      

![tensorboard](tensorboard.gif)

# Build

```
$ make
```

# Usage

The data files are assumed to be stored in the directory specified by `DATA_DIR`. There are two type of files are stored in `DATA_DIR`.

* features_file: It stores the features to be embedded in csv format.
* metadata_file: It stores the metadata such as label or category of each points

The number of data points in `features_file` and `metadata_file` must be same and same order.
You can see the example file in `data/` dire.

```
$ make run \
    DATA_DIR=/path/to/data \
    OPTIONS='--features_file features.csv --metadata_file metadata.csv'
```

It create embedding matrix and launch Tensorboard on the model. Please look at http://localhost:6006/#embeddings.

# License

[MIT License](https://opensource.org/licenses/MIT)


