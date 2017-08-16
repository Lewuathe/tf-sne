#!/usr/bin/env python

import os
import shutil

import tensorflow as tf
import pandas as pd
from tensorflow.contrib.tensorboard.plugins import projector

tf.flags.DEFINE_string(
    'features_file', None, 'Specify the features csv file'
)

tf.flags.DEFINE_string(
    'metadata_file', None, 'Specify the metadata csv file'
)

# tf.flags.DEFINE_integer(
#     'num_data', None, 'Specify the number of samples from data'
# )

tf.flags.DEFINE_string(
    'logdir', 'embeddings', 'Specify the logdir to output embedding metadata'
)

FLAGS = tf.flags.FLAGS

TF_SNE_BASEDIR = '/srv/tf-sne'

def write_embedding(feature_file, metadata_file):
    df = pd.read_csv('{}/data/{}'.format(TF_SNE_BASEDIR, feature_file), header=None)

    embeddings = tf.Variable(df.values, trainable=False, name='embeddings')

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
        writer = tf.summary.FileWriter('./embeddings', sess.graph)
        config = projector.ProjectorConfig()
        embedding = config.embeddings.add()
        embedding.tensor_name = embeddings.name
        embedding.metadata_path = os.path.basename(metadata_file)
        projector.visualize_embeddings(writer, config)

        saver_embed = tf.train.Saver([embeddings])
        saver_embed.save(sess, '{}/embeddings_viz.ckpt'.format('./embeddings'), 1)

    shutil.copy('{}/data/{}'.format(TF_SNE_BASEDIR, metadata_file), '{}/embeddings/{}'.format(TF_SNE_BASEDIR, os.path.basename(metadata_file)))


def main(argv):
    write_embedding(FLAGS.features_file, FLAGS.metadata_file)

if __name__ == '__main__':
    tf.app.run()





