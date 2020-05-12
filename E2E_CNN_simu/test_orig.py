########
# Test steps
# [0] Specify specify 'pre_model_name' in line 26 choosing from 'pre_model_dir'
# [1] Specify 'test_data_dir' in line 37 and Specify 'mask_name' in line39, choosing from 'data_simu/'
# [2] Specify 'batch_size' in line 43
# [3] Run the code
# [4] Results will be stored in 'Result/Validation-Result'


# Environment requirement
# [0] Tensorflow-gpu==1.13.1 (conda install tensorflow-gpu=1.13.1)
# [1] Packages: numpy, yaml, scipy, hdf5storage, matplotlib, math
########
from __future__ import absolute_import

import tensorflow as tf
import yaml
import os
import h5py

from Model.Decoder_Handler import Decoder_Handler


def main():
          
    ### pre-trainded model
    # pre_model_name [modify]
    pre_model_name = 'Decoder-T0427184230-D0.10L0.010-RMSE/models-0.0744-256404'

    pre_model_dir = 'Result\\Model-Config'
    model_filename = os.path.join(os.path.abspath('.'), pre_model_dir, pre_model_name)
    model_config = {'model_filename': model_filename,
                    'result_data': 'Validation-Result',
                    'result_dir': 'Result'}
    
    ### test set
    # test_data_dir [modify]
    test_data_dir = os.path.join(os.path.abspath('..'), 'data_simu\\testing_truth\\')

    # mask_name [modify]
    # mask_name = 'mask_original' 
    mask_name = 'mask_256'
    
    # batch size [modify]
    model_config['batch_size'] = 1

    ## test_data
    data_name = []
    data_name.append('') # placeholder
    data_name.append('')
    data_name.append(test_data_dir)

    ## mask
    # used to initialize the network input
    mask_name = os.path.join(os.path.abspath('..'), 'data_simu', mask_name)

    ## test set    
    dataset_name = (data_name,mask_name)
    

    ### inference
    ## tf config
    tf_config = tf.ConfigProto()
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True

    ## run
    with tf.Session(config=tf_config) as sess:
        # Cube_Decoder = Decoder_Handler_meas(dataset_name=dataset_name, model_config=model_config, sess = sess, is_training=False,Cr=Cr)
        Cube_Decoder = Decoder_Handler(dataset_name=dataset_name, model_config=model_config, sess = sess, is_training=False, is_testing_meas=False)
        Cube_Decoder.test()

if __name__ == '__main__':
    main()
    
    
