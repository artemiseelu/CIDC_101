FROM python:3.9-slim

# 设置环境变量
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TZ=Asia/Shanghai \
    PYTHONPATH=/usr/local/lib/python3.9/site-packages \
    DEBIAN_FRONTEND=noninteractive

# 使用阿里云源（添加重试机制）
RUN set -eux; \
    { \
        echo "deb http://mirrors.aliyun.com/debian/ bullseye main non-free contrib"; \
        echo "deb http://mirrors.aliyun.com/debian-security/ bullseye-security main"; \
        echo "deb http://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib"; \
    } > /etc/apt/sources.list \
    && apt-get update -y || (sleep 2 && apt-get update -y) \
    && apt-get install -y --no-install-recommends \
        libgl1-mesa-glx \
        libglib2.0-0 \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制应用代码和依赖文件
COPY app.py requirements.project.txt /app/

# 配置pip镜像源并安装Python依赖（添加重试机制）
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ || true && \
    pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn || true && \
    for i in {1..3}; do \
        pip install --no-cache-dir -r requirements.project.txt && break || sleep 5; \
    done

# 健康检查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 启动命令
CMD ["python", "app.py"]