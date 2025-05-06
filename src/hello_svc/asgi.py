"""
ASGI应用入口文件
用于支持异步应用的生产环境部署
"""
from hello_svc.views import app

# 导出应用实例供ASGI服务器使用
application = app

if __name__ == "__main__":
    import uvicorn
    
    # 使用uvicorn启动ASGI服务器
    uvicorn.run(
        "asgi:application", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,  # 开发环境中启用热重载
        log_level="info"
    ) 