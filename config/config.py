class Config(object):
    lfw_root = './lfw-align-128'
    lfw_test_list = './lfw_test_pair.txt'
    model = 'che/face_step3_best.pth'
    test_model_path='che/face_step3_best.pth'
    test_batch_size = 16
    input_shape = (1, 112, 112)
    use_gpu = True  # use GPU or not
    gpu_id = '0'
    net_depth=50
    drop_ratio=0.4
    net_mode='ir'
 
