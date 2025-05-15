# GitHub Actions Secrets 配置指南

## 必需的 Secrets

### 1. ALIYUN_USERNAME
阿里云容器镜像服务访问凭证的用户名
```
示例值：your-registry@aliyun.com
实际值：在阿里云容器镜像服务的访问凭证页面获取
```

### 2. ALIYUN_PASSWORD
阿里云容器镜像服务访问凭证的密码
```
示例值：your-registry-password
实际值：在阿里云容器镜像服务的访问凭证页面获取
```

### 3. SSH_PRIVATE_KEY
用于连接部署服务器的 SSH 私钥（整个私钥文件的内容）
```
示例格式：
-----BEGIN OPENSSH PRIVATE KEY-----
MIIEpAIBAAKCAQEAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
... (中间内容) ...
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx==
-----END OPENSSH PRIVATE KEY-----

实际值：使用 cat ~/.ssh/github_deploy 命令查看
```

## 可选的 Secrets

### 4. NOTIFICATION_WEBHOOK
部署通知的 Webhook URL（可选）
```
示例值：https://your-notification-service.com/webhook
实际值：您的通知服务 webhook 地址
```

## 配置步骤

1. 进入您的 GitHub 仓库
2. 点击 "Settings" 标签页
3. 在左侧菜单中找到 "Secrets and variables" -> "Actions"
4. 点击 "New repository secret" 按钮
5. 分别添加上述 secrets：
   - Name: 使用上述大写的名称（如 ALIYUN_USERNAME）
   - Value: 填入对应的值
   - 点击 "Add secret" 保存

## 验证配置

配置完成后，您可以：
1. 提交代码到 main 分支
2. 在 "Actions" 标签页查看工作流运行状态
3. 如果出现错误，检查 Actions 日志中的具体错误信息

## 安全提示

- 永远不要在代码中直接包含这些 secrets
- 定期轮换这些凭证
- 使用最小权限原则配置这些凭证
- 注意保护好您的 SSH 私钥 