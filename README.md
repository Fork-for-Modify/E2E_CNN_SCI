# E2E_CNN_SCI
>  End to End CNN for Reconstruction of Snapshot Compressive Imaging

This repository contains the  codes modified from https://github.com/mq0829/DL-CACTI, which is designed for the paper **Deep Learning for Video Compressive Sensing** (***APL Photonics 5, 030801 (2020)***) by Mu Qiao*, Ziyi Meng*, Jiawei Ma, [Xin Yuan](https://www.bell-labs.com/usr/x.yuan) (*Equal contributions). [[pdf\]](https://aip.scitation.org/doi/pdf/10.1063/1.5140721?download=true) [[doi\]](https://aip.scitation.org/doi/10.1063/1.5140721)



# Structure of directories

- E2E_CNN_simu: The models, codes and results
- data_simu: The simulation data for training or testing. The input data is the scene ground truth ('orig') and mask ('mask'). And when training or testing, the coded measurement ('meas') will be generated automatically with 'orig' (rescale to 0-1 first) and 'mask'.
- data_meas: The simulation data for testing. The input data is the coded measurement ('meas') and mask ('mask')



# Data format

- 'orig': int, 0-255; '.mat' filetype; variable_name(key) = 'patch_save'
- 'mask': float 0-1|binary; '.mat' filetype; variable_name(key) = 'mask'
- 'meas': float; '.mat' filetype; variable_name(key) = 'meas'



# Usage 

## Training

You can train the model by adding your training data to 'data_simu/training_truth/', and most of training parameters can be adjusted in 'Model/Config.yaml'.

## Testing

1. use ’orig‘ as the test input data：
   - Put the ’orig‘  in 'data_simu/testing_truth/', and put the 'mask' in 'data_simu/'
   - Open and modify 'E2E_CNN_simu/test_orig.py' according to the instructions in the beginning of the code and then run it.
   - The results will be saved as 'E2E_CNN_simu/Result/Validation-Result/Test_orig_result_i.mat'
2. use ’meas‘ as the test input data：
   - Put the data in 'data_meas/meas/', and put the 'mask' in 'data_mask/mask/'
   - Open and modify 'E2E_CNN_simu/test_meas.py' according to the instructions in the beginning of the code and then run it.
   - The results will be saved as 'E2E_CNN_simu/Result/Validation-Result/Test_meas_result_i.mat'



# Reference

**Deep Learning for Video Compressive Sensing** (***APL Photonics 5, 030801 (2020)***) by Mu Qiao*, Ziyi Meng*, Jiawei Ma, [Xin Yuan](https://www.bell-labs.com/usr/x.yuan) (*Equal contributions). [[pdf\]](https://aip.scitation.org/doi/pdf/10.1063/1.5140721?download=true) [[doi\]](https://aip.scitation.org/doi/10.1063/1.5140721)

 https://github.com/mq0829/DL-CACTI

https://github.com/Phoenix-V/tensor-admm-net-sci