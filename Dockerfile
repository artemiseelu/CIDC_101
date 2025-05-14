# 使用本地构建的基础镜像
FROM local-base-image:latest

# 切换到root用户安装依赖
USER root

# 复制应用代码
COPY --chown=appuser:appuser . /app/

# 安装项目依赖
COPY --chown=appuser:appuser requirements.project.txt /app/
RUN pip install --no-cache-dir -r requirements.project.txt

# 切换回普通用户
USER appuser

# 健康检查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 启动命令
CMD ["python", "app.py"] 