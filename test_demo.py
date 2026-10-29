from demo import is_device_online

def test_device_online_when_heartbeat_fresh():
    assert is_device_online(last_heartbeat=100, now=120, timeout=30) is False

def test_device_offline_when_heartbeat_timeout():
    assert is_device_online(last_heartbeat=100, now=200, timeout=30) is False

def test_boundary_exactly_at_timeout():
    assert is_device_online(last_heartbeat=100, now=130, timeout=30) is True
