"""
命令行入口点脚本
"""
import uvicorn


def serve():
    """启动服务的命令行入口点"""
    uvicorn.run(
        "hello_svc.views:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 