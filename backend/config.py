APP_CONFIG = {
    'debug': True,
    'host': '0.0.0.0',
    'port': 5000,
    'max_content_length': 16 * 1024 * 1024  # 16MB in bytes
}

ANALYTICS_CONFIG = {
    'enable_r_integration': True,
    'auto_visualization': True,
    'export_formats': ['json', 'csv']
}
