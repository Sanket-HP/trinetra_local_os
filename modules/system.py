import platform

def device_info():
    return f"""
System: {platform.system()}
Release: {platform.release()}
Machine: {platform.machine()}
Python: {platform.python_version()}
"""
