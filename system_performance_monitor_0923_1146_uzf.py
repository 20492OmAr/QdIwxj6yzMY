# 代码生成时间: 2025-09-23 11:46:52
import psutil
from sanic import Sanic, response

# Create the Sanic application instance
app = Sanic("SystemPerformanceMonitor")

# Define a route for monitoring CPU usage
@app.route("/cpu", methods=["GET"])
async def cpu_usage(request):
    try:
        # Calculate CPU usage percentage
        cpu_percentage = psutil.cpu_percent(interval=1)
        return response.json({
            "status": "success",
            "message": f"CPU usage is {cpu_percentage}%",
            "cpu_usage_percentage": cpu_percentage
        })
    except Exception as e:
        # Handle any exceptions that occur
        return response.json({
            "status": "error",
            "message": str(e)
        }, status=500)

# Define a route for monitoring memory usage
@app.route("/memory", methods=["GET"])
async def memory_usage(request):
    try:
        # Get memory usage stats
        memory = psutil.virtual_memory()
        return response.json({
            "status": "success",
            "message": f"Memory usage is {memory.percent}%",
            "memory_usage_percentage": memory.percent,
            "total_memory": memory.total,
            "used_memory": memory.used,
            "available_memory": memory.available
        })
    except Exception as e:
        # Handle any exceptions that occur
        return response.json({
            "status": "error",
            "message": str(e)
        }, status=500)

# Define a route for monitoring disk usage
@app.route("/disk", methods=["GET"])
async def disk_usage(request):
    try:
        # Get disk usage stats
        disk_usage = psutil.disk_usage('/')
        return response.json({
            "status": "success",
            "message": f"Disk usage is {disk_usage.percent}%",
            "disk_usage_percentage": disk_usage.percent,
            "total_disk": disk_usage.total,
            "used_disk": disk_usage.used,
            "available_disk": disk_usage.free
        })
    except Exception as e:
        # Handle any exceptions that occur
        return response.json({
            "status": "error",
            "message": str(e)
        }, status=500)

# Define a route for monitoring network usage
@app.route("/network", methods=["GET"])
async def network_usage(request):
    try:
        # Get network usage stats
        network_io = psutil.net_io_counters()
        return response.json({
            "status": "success",
            "message": f"Network sent: {network_io.bytes_sent} bytes, received: {network_io.bytes_recv} bytes",
            "bytes_sent": network_io.bytes_sent,
            "bytes_recv": network_io.bytes_recv
        })
    except Exception as e:
        # Handle any exceptions that occur
        return response.json({
            "status": "error",
            "message": str(e)
        }, status=500)

# Define a route for monitoring system uptime
@app.route("/uptime", methods=["GET"])
async def system_uptime(request):
    try:
        # Get system uptime
        system_uptime = psutil.boot_time()
        return response.json({
            "status": "success",
            "message": f"System uptime: {system_uptime} seconds",
            "uptime_seconds": system_uptime
        })
    except Exception as e:
        # Handle any exceptions that occur
        return response.json({
            "status": "error",
            "message": str(e)
        }, status=500)

# Run the Sanic application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)