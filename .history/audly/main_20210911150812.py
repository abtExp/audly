import projectaile as pai

import tensorflow as tf

cfg = pai.CONFIG()

data_pipeline = pai.DATA_PIPELINE(cfg)

model = tf.keras.models.Model()

model_pipeline = pai.MODEL_PIPELINE(cfg, model)

engine = pai.ENGINE(data_pipeline, model_pipeline)

# run training
engine.run()

engine.run(mode='infer')