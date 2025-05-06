# 变更日志

本项目的所有显著变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 新增

- 添加了`src/wsgi.py`文件作为WSGI应用入口
- 添加了`src/asgi.py`文件作为ASGI应用入口，支持异步应用部署
- 添加了`scripts.py`和命令行入口点，通过`uv run uvexercise`可直接启动服务
- 添加了`.gitignore`文件，忽略Python缓存、虚拟环境和其他临时文件

## [0.1.0] - 2023-10-15

### 新增

- 创建基本项目结构
- 使用FastAPI实现简单的Hello World API
- 添加单元测试
- 配置pyproject.toml管理依赖
- 更新README.md包含详细使用说明
- 添加CHANGELOG.md记录版本变更 