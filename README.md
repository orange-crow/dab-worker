# DAB - 分布式智能体评测平台

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen.svg)](https://nodejs.org/)
[![Python Version](https://img.shields.io/badge/python-3.13.3-blue.svg)](https://python.org/)

DAB（Decentralized Agent Benchmarking）是一个基于 iExec 去中心化计算平台的智能体评测系统。该系统通过可信执行环境（TEE）确保评测过程的透明性和安全性，为智能体性能评估提供可靠的分布式计算解决方案。

## 🌟 项目特色

- 🚀 **分布式计算**: 基于 iExec 网络的分布式评测任务执行
- 🔒 **安全可信**: TEE 环境确保数据安全和计算透明性
- 📊 **完整监控**: 任务执行全生命周期监控和追踪
- 🔐 **权限管理**: 基于 JWT 的用户认证和权限控制
- 📈 **性能优化**: 智能任务调度和资源管理
- 🛡️ **错误恢复**: 完善的错误处理和自动重试机制
- 🐳 **容器化部署**: 完整的 Docker 和 Docker Compose 支持

## 🏗️ 系统架构

DAB 系统由三个核心组件组成：

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   DAB Core      │    │   DAB Server    │    │   DAB Worker    │
│                 │    │                 │    │                 │
│ • iExec SDK     │◄──►│ • 任务管理      │◄──►│ • 评测执行      │
│ • 应用部署      │    │ • 用户认证      │    │ • TEE 环境      │
│ • 任务运行      │    │ • 数据存储      │    │ • 结果处理      │
│ • API 接口      │    │ • 监控日志      │    │ • 安全计算      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 组件说明

- **DAB Core**: iExec SDK 集成层，负责应用的测试、部署和运行
- **DAB Server**: 中心化服务平台，提供任务管理、用户认证和数据存储
- **DAB Worker**: 分布式评测执行器，在 TEE 环境中安全执行评测任务

## 🚀 快速开始

### 环境要求

- Node.js v20+
- Python 3.13.3
- Docker & Docker Compose
- PostgreSQL 12+
- Redis 6+
- iExec 钱包和私钥

### 一键启动（推荐）

```bash
# 克隆项目
git clone <repository-url>
cd dab

# 启动所有服务
docker-compose up -d

# 验证服务状态
curl http://localhost:3000/api/v1/health
```

### 分步启动

#### 1. 启动 DAB Server

```bash
cd dab-server

# 安装依赖
npm install

# 配置环境变量
cp env.example .env
# 编辑 .env 文件，配置数据库、Redis、iExec 等参数

# 启动服务
npm run dev
```

#### 2. 启动 DAB Core

```bash
cd dab-core

# 安装依赖
npm install

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置 iExec 私钥等参数

# 启动服务
npm run dev
```

#### 3. 部署 DAB Worker

```bash
cd dab-worker

# 安装依赖
pip install -r requirements.txt

# 配置 iExec 应用
# 编辑 iapp.config.json 文件

# 部署到 iExec 网络
iexec app deploy
```

## 📖 详细文档

### 核心组件文档

- [DAB Core 文档](./dab-core/README.md) - iExec SDK 集成和 API 接口
- [DAB Server 文档](./dab-server/README.md) - 中心化服务平台
- [DAB Worker 文档](./dab-worker/README.md) - 分布式评测执行器

### 快速指南

- [DAB Server 快速启动](./dab-server/QUICKSTART.md) - 5分钟快速上手
- [环境配置说明](./dab-core/ENV_CONFIG.md) - 详细的环境变量配置

## 🔧 API 接口

### 认证接口

```http
POST /api/v1/auth/register    # 用户注册
POST /api/v1/auth/login       # 用户登录
```

### 任务管理接口

```http
POST   /api/v1/tasks                    # 创建评测任务
GET    /api/v1/tasks/{taskId}/status    # 查询任务状态
POST   /api/v1/tasks/{taskId}/deploy    # 部署任务
POST   /api/v1/tasks/{taskId}/execute   # 执行任务
GET    /api/v1/tasks/{taskId}/results   # 获取任务结果
```

### iExec 集成接口

```http
POST /api/iapp/test      # 测试 iExec 应用
POST /api/iapp/deploy    # 部署 iExec 应用
POST /api/iapp/run       # 运行 iExec 应用
```

### 健康检查接口

```http
GET /api/v1/health           # 基础健康检查
GET /api/v1/health/detailed  # 详细健康检查
```

## 💡 使用示例

### 创建评测任务

```bash
curl -X POST http://localhost:3000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "taskName": "智能体性能评测",
    "description": "基于标准数据集的大语言模型性能评估",
    "appId": "0x456def...",
    "llmConfigs": {
      "model": "gpt-4",
      "temperature": 0.7,
      "maxTokens": 4096
    },
    "datasetConfig": {
      "urls": ["https://data.gov/reference-corpus.csv"],
      "format": "csv"
    },
    "resourceRequirements": {
      "dockerHubName": "dab/agent-evaluator",
      "minCpuCores": 4,
      "minMemoryGB": 8
    }
  }'
```

### 部署和运行任务

```bash
# 部署任务
curl -X POST http://localhost:3000/api/v1/tasks/{taskId}/deploy \
  -H "Authorization: Bearer YOUR_TOKEN"

# 执行任务
curl -X POST http://localhost:3000/api/v1/tasks/{taskId}/execute \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "executionParams": {
      "maxWorkers": 10,
      "batchSize": 100,
      "timeout": 3600
    }
  }'
```

## 🛠️ 开发指南

### 项目结构

```
dab/
├── dab-core/           # iExec SDK 集成层
│   ├── src/           # 源代码
│   ├── test/          # 测试文件
│   └── package.json   # Node.js 依赖
├── dab-server/        # 中心化服务平台
│   ├── src/           # 源代码
│   ├── test/          # 测试文件
│   ├── docker-compose.yml  # Docker 配置
│   └── package.json   # Node.js 依赖
└── dab-worker/        # 分布式评测执行器
    ├── src/           # Python 源代码
    ├── requirements.txt  # Python 依赖
    └── iapp.config.json # iExec 应用配置
```

### 开发命令

```bash
# 运行测试
npm test                # 在 dab-core 或 dab-server 目录下
python -m pytest       # 在 dab-worker 目录下

# 代码检查
npm run lint           # ESLint 检查
npm run lint:fix       # 自动修复 ESLint 问题

# 启动开发服务器
npm run dev            # 开发模式启动
npm start              # 生产模式启动
```

### 测试

```bash
# 运行所有测试
npm test

# 运行测试并生成覆盖率报告
npm run test:coverage

# 监听模式运行测试
npm run test:watch
```

## 🐳 部署指南

### Docker 部署

```bash
# 构建所有镜像
docker-compose build

# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

### 生产环境配置

1. **环境变量配置**
   ```env
   NODE_ENV=production
   DB_HOST=your-db-host
   REDIS_HOST=your-redis-host
   IEXEC_WALLET_PRIVATE_KEY=your-production-key
   JWT_SECRET=your-production-secret
   ```

2. **安全配置**
   - 使用强密码和密钥
   - 配置 HTTPS
   - 设置防火墙规则
   - 定期备份数据

3. **监控和日志**
   - 配置日志轮转
   - 设置监控告警
   - 定期健康检查

## 🔒 安全考虑

- **数据加密**: 所有敏感数据加密传输和存储
- **访问控制**: 基于 JWT 的用户认证和授权
- **TEE 安全**: 利用可信执行环境确保计算安全
- **审计日志**: 记录所有关键操作和访问
- **限流保护**: 防止 API 滥用和 DDoS 攻击

## 📊 监控和运维

### 健康检查

```bash
# 基础健康检查
curl http://localhost:3000/api/v1/health

# 详细健康检查
curl http://localhost:3000/api/v1/health/detailed
```

### 日志管理

```bash
# 查看应用日志
tail -f logs/combined-$(date +%Y-%m-%d).log

# 查看错误日志
tail -f logs/error-$(date +%Y-%m-%d).log

# 查看 Docker 日志
docker-compose logs -f dab-server
```

### 性能监控

系统提供详细的性能监控指标：
- 请求响应时间
- 任务执行统计
- 系统资源使用情况
- 数据库和 Redis 连接状态

## 🐛 故障排除

### 常见问题

1. **数据库连接失败**
   ```bash
   # 检查 PostgreSQL 状态
   docker-compose logs postgres
   
   # 重启数据库
   docker-compose restart postgres
   ```

2. **Redis 连接失败**
   ```bash
   # 检查 Redis 状态
   docker-compose logs redis
   
   # 重启 Redis
   docker-compose restart redis
   ```

3. **iExec 连接失败**
   - 检查钱包私钥是否正确
   - 验证网络配置
   - 确认 iExec 链设置

4. **任务执行失败**
   - 检查 iExec 网络状态
   - 验证任务配置参数
   - 查看 Worker 日志

### 重置环境

```bash
# 停止所有服务
docker-compose down

# 删除数据卷（注意：会丢失所有数据）
docker-compose down -v

# 重新启动
docker-compose up -d
```

## 🤝 贡献指南

我们欢迎社区贡献！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 开发规范

- 遵循 ESLint 代码规范
- 编写单元测试
- 更新相关文档
- 确保所有测试通过

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- **项目维护团队**: DAB 开发团队
- **文档版本**: v1.0
- **最后更新**: 2025年1月

## 🙏 致谢

感谢以下开源项目和技术：

- [iExec](https://iex.ec/) - 去中心化计算平台
- [Node.js](https://nodejs.org/) - JavaScript 运行时
- [Express.js](https://expressjs.com/) - Web 应用框架
- [PostgreSQL](https://postgresql.org/) - 关系型数据库
- [Redis](https://redis.io/) - 内存数据库
- [Docker](https://docker.com/) - 容器化平台

---

**注意**: 这是一个开发/测试环境配置。生产环境部署请参考完整的部署指南和安全配置。
