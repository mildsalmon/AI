from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())

# [name: "/device:CPU:0"
# device_type: "CPU"
# memory_limit: 268435456
# locality {
# }
# incarnation: 7214277798853684827
# , name: "/device:GPU:0"
# device_type: "GPU"
# memory_limit: 8967317095
# locality {
#   bus_id: 1
#   links {
#   }
# }
# incarnation: 12893995977759368046
# physical_device_desc: "device: 0, name: GeForce RTX 3080, pci bus id: 0000:01:00.0, compute capability: 8.6"
# ]


# import tensorflow as tf
#
# # config = tf.ConfigProto(device_count= {'CPU':0}, log_device_placement=True)
#
# tf.debugging.set_log_device_placement(True)
#
# print(tf.__version__)
#
# with tf.device('/device:GPU:0'):
#     hello = tf.constant("H")
#
#     sess = tf.Session()
#
#     # tf.Session(config=config)
#     print(sess.run(hello))