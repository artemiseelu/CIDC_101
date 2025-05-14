# Docker 多层构建示例

本项目演示如何使用 Docker 多层构建来优化 Python 应用的构建过程，特别适用于包含 PyTorch 等大型依赖的项目。

## 项目结构

    .
    ├── README.md               # 本文档
    ├── Dockerfile.base         # 基础镜像配置
    ├── Dockerfile             # 应用镜像配置
    ├── app.py                # 示例FastAPI应用
    ├── requirements.base.txt    # 基础依赖（PyTorch等）
    └── requirements.project.txt # 项目特定依赖

## 本地测试步骤

### 1. 构建基础镜像

在项目根目录执行：

    docker build -t local-base-image:latest -f Dockerfile.base .

此步骤会：
- 安装 PyTorch 等基础依赖
- 创建基础运行环境
- 设置必要的系统配置

### 2. 构建应用镜像

在项目根目录执行：

    docker build -t my-app:latest .

此步骤会：
- 基于基础镜像构建
- 只添加项目代码和轻量级依赖
- 配置应用运行环境

### 3. 运行容器

启动应用：

    docker run -d -p 8000:8000 --name my-app my-app:latest

### 4. 测试应用

测试 API 端点：

    curl http://localhost:8000/
    curl http://localhost:8000/health

预期输出包含：
- PyTorch 版本信息
- 随机生成的张量
- 健康状态检查

## 开发流程

### 修改依赖

1. 基础依赖修改：
   - 更新 requirements.base.txt
   - 重新构建基础镜像
   - 重新构建应用镜像

2. 项目依赖修改：
   - 更新 requirements.project.txt
   - 只需重新构建应用镜像

### 更新应用代码

1. 修改 app.py
2. 直接重新构建应用镜像：

    docker build -t my-app:latest .

## 清理命令

停止和删除容器：

    docker stop my-app
    docker rm my-app

删除镜像：

    docker rmi my-app:latest
    docker rmi local-base-image:latest

## 生产环境部署

1. 修改 Dockerfile 中的基础镜像地址为阿里云地址：

    FROM crpi-xxxx.cn-shanghai.personal.cr.aliyuncs.com/your-namespace/base-image:latest

2. 确保 GitHub Actions 配置正确：
   - base-image.yml 用于构建基础镜像
   - deploy.yml 用于部署应用

## 注意事项

1. 基础镜像构建时间较长，但只需构建一次
2. 应用镜像构建快速，适合频繁更新
3. 确保 requirements.base.txt 和 requirements.project.txt 依赖不重复
4. 生产环境部署前检查 Dockerfile 中的基础镜像地址

## 常见问题

1. 构建失败：
   - 检查网络连接
   - 确认依赖版本兼容性
   - 查看构建日志

2. 运行错误：
   - 确认端口映射正确
   - 检查日志输出
   - 验证健康检查状态

## 贡献指南

1. Fork 本仓库
2. 创建功能分支
3. 提交更改
4. 发起 Pull Request

## 许可证

MIT 