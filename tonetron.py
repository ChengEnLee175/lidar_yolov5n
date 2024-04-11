import netron
 

onnx_path = "runs/train/yolov5n_ori/weights/best.onnx"
 
netron.start(onnx_path)