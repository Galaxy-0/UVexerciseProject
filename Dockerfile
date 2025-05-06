FROM python:3.10-slim

WORKDIR /app

# 设置Python环境
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 安装uv
RUN pip install uv --no-cache-dir

# 复制项目文件
COPY . /app/

# 使用uv和清华镜像源安装依赖
RUN uv pip install --mirror https://pypi.tuna.tsinghua.edu.cn/simple -e .

# 暴露端口
EXPOSE 8000

# 启动服务
CMD ["python", "-m", "src.hello_svc.views"] 