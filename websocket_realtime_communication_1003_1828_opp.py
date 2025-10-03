# 代码生成时间: 2025-10-03 18:28:45
import asyncio
from sanic import Sanic, response
from sanic.websocket import WebSocketProtocol
from sanic.exceptions import ServerError, ServerErrorMiddleware
from sanic.log import logger

# 初始化Sanic应用
app = Sanic('WebSocket Real-time Communication')

# 定义WebSocket路由
@app.websocket('/ws')
async def websocket_handler(request, ws: WebSocketProtocol):
    # 连接建立时的处理逻辑
    await ws.send('Welcome to the WebSocket server!')
    logger.info('WebSocket connection established')

    # 异步循环等待接收消息
    while True:
        try:
            # 接收客户端发送的消息
            message = await ws.recv()
            if message is None:
                # 如果没有接收到消息，退出循环
                break
            # 将接收到的消息发送回客户端
            await ws.send(message)
        except Exception as e:
            # 异常处理
            logger.error(f'WebSocket error: {e}')
            break

    # 连接关闭时的处理逻辑
    logger.info('WebSocket connection closed')

# 错误处理
@app.exception(ServerError)
async def handle_server_error(request, exception: ServerError):
    logger.error(f'Server error: {exception}')
    return response.json({'error': 'Internal Server Error'}, status=500)

# 错误处理中间件
@app.middleware('request')
async def error_logging_middleware(request):
    try:
        yield
    except ServerError as e:
        logger.error(f'Server error: {e}')
        raise e

# 运行Sanic应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
