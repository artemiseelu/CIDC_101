from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import numpy as np
from ultralytics import YOLO
import uvicorn
from typing import List, Optional
import time

app = FastAPI(
    title="CIDC API",
    description="CIDC Machine Learning API Service",
    version="1.0.0"
)

class PredictionInput(BaseModel):
    image_url: str
    confidence_threshold: Optional[float] = 0.5

class PredictionResult(BaseModel):
    predictions: List[dict]
    processing_time: float
    model_info: dict

@app.get("/")
def read_root():
    # 使用torch验证基础依赖是否正确安装
    tensor = torch.rand(3, 3)
    return {
        "message": "Welcome to CIDC API",
        "status": "running",
        "torch_version": torch.__version__,
        "cuda_available": torch.cuda.is_available(),
        "tensor_sample": tensor.tolist()
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "dependencies": {
            "torch": torch.__version__,
            "numpy": np.__version__,
            "cuda_available": torch.cuda.is_available()
        }
    }

@app.post("/predict", response_model=PredictionResult)
async def predict(input_data: PredictionInput):
    try:
        start_time = time.time()
        
        # 这里添加您的模型预测逻辑
        # 示例返回
        predictions = [
            {
                "class": "example",
                "confidence": 0.95,
                "bbox": [100, 100, 200, 200]
            }
        ]
        
        processing_time = time.time() - start_time
        
        return PredictionResult(
            predictions=predictions,
            processing_time=processing_time,
            model_info={
                "name": "YOLO",
                "version": "v8",
                "type": "object_detection"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model/info")
def get_model_info():
    return {
        "model_name": "YOLO",
        "model_version": "v8",
        "supported_tasks": ["object_detection"],
        "input_format": "image",
        "output_format": "bounding_boxes",
        "performance_metrics": {
            "accuracy": 0.95,
            "inference_time": "50ms"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 