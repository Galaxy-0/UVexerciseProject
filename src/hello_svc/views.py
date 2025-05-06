from fastapi import FastAPI

# 创建FastAPI应用实例
app = FastAPI(
    title="Hello World API",
    description="一个简单的Hello World API示例",
    version="0.1.0"
)

# 定义一个可独立使用的hello_world函数
def get_hello_message():
    """
    返回一个简单的Hello World消息
    
    Returns:
        dict: 包含问候消息的字典
    """
    return {"message": "Hello, World!"}

# 定义根路由处理函数
@app.get("/")
async def hello_world():
    """
    返回一个简单的Hello World消息
    
    Returns:
        dict: 包含问候消息的字典
    """
    return get_hello_message()

# 如果直接运行此文件，则启动服务器
if __name__ == "__main__":
    import uvicorn
    # 使用uvicorn启动服务器，监听所有网络接口的8000端口
    uvicorn.run(app, host="0.0.0.0", port=8000)
