import pytest
from src.hello_svc.views import app, get_hello_message

def test_app_instance():
    """测试应用实例是否正确创建"""
    assert app.title == "Hello World API"
    assert app.version == "0.1.0"

def test_get_hello_message():
    """测试 get_hello_message 函数的返回值"""
    response = get_hello_message()
    assert response == {"message": "Hello, World!"} 