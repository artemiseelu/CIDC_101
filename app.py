from fastapi import FastAPI
import torch  # 验证基础镜像中的依赖
import numpy as np
import uvicorn
from ultralytics import YOLO

app = FastAPI()

@app.get("/")
def read_root():
    # 使用torch验证基础依赖是否正确安装
    tensor = torch.rand(3, 3)
    return {
        "message": "Hello World",
        "torch_version": torch.__version__,
        "tensor_sample": tensor.tolist()
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 