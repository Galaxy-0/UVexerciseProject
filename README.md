# UVexerciseProject

一个用来熟悉uv包管理工具的项目，使用FastAPI创建了一个简单的Hello World服务。

## 项目结构

```
UVexerciseProject/
├── src/
│   └── hello_svc/
│       ├── __init__.py
│       ├── views.py
│       └── test_views.py
├── pyproject.toml
└── README.md
```

## 环境设置

本项目使用`uv`包管理工具管理依赖。

### 安装依赖

使用清华镜像源安装依赖：

```bash
uv pip install --mirror https://pypi.tuna.tsinghua.edu.cn/simple -e .
```

安装测试依赖：

```bash
uv pip install --mirror https://pypi.tuna.tsinghua.edu.cn/simple -e ".[test]"
```

## 运行服务

```bash
cd src
python -m hello_svc.views
```

服务将在 http://localhost:8000 运行。

## 运行测试

```bash
pytest
```

或者运行测试并生成覆盖率报告：

```bash
pytest --cov
```

## 使用Docker运行

### 构建镜像

```bash
docker build -t hello_svc .
```

### 运行容器

```bash
docker run -p 8000:8000 hello_svc
```

## API文档

服务运行后，可以在以下地址查看API文档：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 版本历史

请查看 [CHANGELOG.md](CHANGELOG.md) 文件了解版本变更记录。
