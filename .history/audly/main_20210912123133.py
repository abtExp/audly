import projectaile as pai

import tensorflow as tf

cfg = pai.CONFIG()

data_pipeline = pai.DATA_PIPELINE(cfg)

model = tf.keras.models.Model()

model_pipeline = pai.MODEL_PIPELINE(cfg, model)

engine = pai.ENGINE(data_pipeline, model_pipeline)

# run training
engine.run()

# save configs and pipelines and models
engine.dump()

# make predictions
preds = engine.run(new_example, mode='infer')