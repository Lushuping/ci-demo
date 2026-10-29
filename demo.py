def is_device_online(last_heartbeat, now, timeout=30):
    """判断设备是否在线：心跳超时则离线"""
    return now - last_heartbeat <= timeout
