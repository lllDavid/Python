import random
import string
# NOTE: Currently this assumes lists like media.audio_codecs, time_zone.languages etc. are always same length

device_base_dicts = {}

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_latitude():
    return round(random.uniform(-90, 90), 6)

def random_longitude():
    return round(random.uniform(-180, 180), 6)

def random_bool():
    return random.choice([True, False])

def random_choice(choices):
    return random.choice(choices)

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_float(low=0, high=100):
    return round(random.uniform(low, high), 2)

def random_int(low=0, high=1000):
    return random.randint(low, high)

def randomize_browser_info():
    possible_browsers = [
        'Chrome 137.0', 'Firefox 92.0', 'Edge 90.0', 'Safari 14.1',
        'Opera 80.0', 'Brave 1.35', 'Vivaldi 4.3'
    ]
    return {
        'browser.browser': random.choice(possible_browsers)
    }

def randomize_hardware_os():
    possible_os = [
        'Windows 10.0', 'Windows 11.0', 'Ubuntu 20.04 LTS', 'Ubuntu 22.04 LTS',
        'macOS 11.2 Big Sur', 'macOS 12.0 Monterey', 'Fedora 35', 'Debian 11',
        'CentOS 8', 'Red Hat Enterprise Linux 8', 'Arch Linux', 'Linux Mint 20',
        'Android 12', 'iOS 15.4', 'Chrome OS 91', 'FreeBSD 13.0'
    ]
    return {
        'hardware.os': random.choice(possible_os)
    }

def randomize_indexeddb_db():
    possible_dbs = [
        'test',
        'mainDB',
        'user_data',
        'app_cache',
        'session_store',
        'preferences',
        'analyticsDB',
        'localStorageDB',
        'tempData',
        'configDB',
    ]
    db = random.choice(possible_dbs)
    
    return {
        'storage.indexeddb_dbs.0': db
    }

def random_time_zone_info():
    tz = random_choice([
        'Europe/Berlin', 'America/New_York', 'Asia/Tokyo', 'Europe/London',
        'America/Los_Angeles', 'Asia/Kolkata', 'Australia/Sydney',
        'America/Chicago', 'Europe/Paris', 'Asia/Shanghai',
        'America/Sao_Paulo', 'Africa/Johannesburg', 'Pacific/Auckland', 'Asia/Dubai', 'Europe/Moscow'
    ])
    timezone_offsets = [
        -720, -660, -600, -570, -540, -480, -420, -360, -300, -270, -240, -210, -180, -150,
        -120, -60, 0, 60, 90, 120, 180, 210, 240, 270, 300, 330, 345, 360, 390, 420, 480,
        525, 540, 570, 600, 630, 660, 690, 720, 765, 780, 840
    ]
    offset = random_choice(timezone_offsets)
    languages = ['en-US', 'en']
    return {
        'time_zone.time_zone': tz,
        'time_zone.timezone_offset': offset,
        'time_zone.languages.length': len(languages),
        'time_zone.languages.0': languages[0],
        'time_zone.languages.1': languages[1],
    }

def randomize_http_header_fingerprint():
    http_versions = ['HTTP/1.0', 'HTTP/1.1', 'HTTP/2', 'HTTP/3']
    tls_protocols = ['TLS 1.2', 'TLS 1.3']
    tls_cipher_suites = [
        'TLS_AES_128_GCM_SHA256',
        'TLS_AES_256_GCM_SHA384',
        'TLS_CHACHA20_POLY1305_SHA256',
        'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256',
        'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384'
    ]
    referers = [
        'https://www.google.com/search?q=test',
        'https://www.example.com/',
        'https://news.ycombinator.com/',
        'https://twitter.com/',
        'https://github.com/'
    ]

    header_count = random.randint(6, 15)
    unusual_headers_count = random.randint(0, 3)

    return {
        'http_header_fingerprint.header_count': header_count,
        'http_header_fingerprint.http_version': random.choice(http_versions),
        'http_header_fingerprint.tls_protocol': random.choice(tls_protocols),
        'http_header_fingerprint.tls_cipher_suite': random.choice(tls_cipher_suites),
        'http_header_fingerprint.headers_present.length': header_count,
        'http_header_fingerprint.unusual_headers.length': unusual_headers_count,
        'http_header_fingerprint.referer': random.choice(referers),
    }

def randomize_graphics_info():
    vendors = {
        'NVIDIA': ['NVIDIA GeForce RTX 3080', 'NVIDIA GeForce GTX 1080', 'NVIDIA Quadro RTX 4000'],
        'AMD': ['AMD Radeon RX 6800', 'AMD Radeon RX 5700 XT', 'AMD Radeon Vega 56'],
        'Intel': ['Intel Iris Xe', 'Intel UHD Graphics 620', 'Intel HD Graphics 530']
    }
    vendor = random.choice(list(vendors.keys()))
    gpu_model = random.choice(vendors[vendor])
    
    webgl_renderer = f"ANGLE ({vendor}, {gpu_model} Direct3D11 vs_5_0 ps_5_0, D3D11)"
    webgl_vendor = f"Google Inc. ({vendor})"

    possible_extensions = [
        'ANGLE_instanced_arrays', 'EXT_blend_minmax', 'EXT_clip_control',
        'EXT_color_buffer_half_float', 'EXT_depth_clamp', 'EXT_disjoint_timer_query',
        'EXT_float_blend', 'EXT_frag_depth', 'EXT_polygon_offset_clamp',
        'EXT_shader_texture_lod', 'EXT_texture_compression_bptc',
        'EXT_texture_compression_rgtc', 'EXT_texture_filter_anisotropic',
        'EXT_texture_mirror_clamp_to_edge', 'EXT_sRGB', 'KHR_parallel_shader_compile',
        'OES_element_index_uint', 'OES_fbo_render_mipmap', 'OES_standard_derivatives',
        'OES_texture_float', 'OES_texture_float_linear', 'OES_texture_half_float',
        'OES_texture_half_float_linear', 'OES_vertex_array_object',
        'WEBGL_blend_func_extended', 'WEBGL_color_buffer_float',
        'WEBGL_compressed_texture_s3tc', 'WEBGL_compressed_texture_s3tc_srgb',
        'WEBGL_debug_renderer_info', 'WEBGL_debug_shaders', 'WEBGL_depth_texture',
        'WEBGL_draw_buffers', 'WEBGL_lose_context', 'WEBGL_multi_draw',
        'WEBGL_polygon_mode'
    ]
    extensions_count = random.randint(20, 35)
    extensions = random.sample(possible_extensions, extensions_count)

    possible_features = [
        'float32-blendable', 'depth32float-stencil8', 'rg11b10ufloat-renderable',
        'bgra8unorm-storage', 'depth-clip-control', 'texture-compression-bc',
        'dual-source-blending', 'timestamp-query', 'clip-distances',
        'float32-filterable', 'indirect-first-instance', 'subgroups'
    ]
    features_count = random.randint(8, 12)
    features = random.sample(possible_features, features_count)

    info = {
        'graphics.webgl_renderer': webgl_renderer,
        'graphics.webgl_vendor': webgl_vendor,
        'graphics.webgl_extensions.length': extensions_count,
        'graphics.webgpu_adapter.name': None,
        'graphics.webgpu_adapter.features.length': features_count,
        'graphics.webgpu_adapter.isFallbackAdapter': False,
    }
    for i, ext in enumerate(extensions):
        info[f'graphics.webgl_extensions.{i}'] = ext
    for i, feat in enumerate(features):
        info[f'graphics.webgpu_adapter.features.{i}'] = feat

    return info

def randomize_ip_details():
    return {
        'ip.ip_address': random_ip(),
        'ip.details.city': random_choice([
            'New York', 'London', 'Paris', 'Berlin', 'Tokyo', 'Toronto', 'Sydney', 'Moscow',
            'San Francisco', 'Los Angeles', 'Chicago', 'Boston', 'Madrid', 'Rome', 'Vienna',
            'Amsterdam', 'Brussels', 'Copenhagen', 'Stockholm', 'Oslo', 'Zurich', 'Geneva',
            'Dubai', 'Singapore', 'Seoul', 'Beijing', 'Shanghai', 'Hong Kong', 'Bangkok',
            'Mumbai', 'Delhi', 'São Paulo', 'Buenos Aires', 'Mexico City', 'Cape Town',
            'Johannesburg', 'Nairobi', 'Helsinki', 'Warsaw', 'Lisbon', 'Dublin', 'Prague',
            'Budapest', 'Athens', 'Istanbul', 'Kuala Lumpur', 'Jakarta', 'Manila',
            'Vancouver', 'Montreal', 'Melbourne', 'Brisbane', 'Wellington', 'Lima',
            'Bogotá', 'Caracas', 'Santiago', 'Cairo', 'Riyadh', 'Doha', 'Tehran',
            'Baghdad', 'Kuwait City', 'Karachi', 'Lagos', 'Accra', 'Casablanca'
        ]),
        'ip.details.region': random_choice([
            'California', 'Bavaria', 'Ontario', 'Queensland', 'New South Wales', 'Île-de-France',
            'Catalonia', 'Lombardy', 'Texas', 'Scotland', 'British Columbia', 'Andalusia',
            'Gauteng', 'São Paulo State', 'Hokkaido', 'Punjab', 'Karnataka', 'Maharashtra',
            'Gujarat', 'New York State', 'Florida', 'Tuscany', 'Yorkshire', 'Saxony',
            'Alberta', 'Lazio', 'Western Cape', 'Northern Territory', 'Valencia',
            'Mazovia', 'Flanders', 'Navarre', 'Hessen', 'Tyrol', 'Brittany',
            'Navarra', 'Kerala', 'West Bengal', 'Zhejiang', 'Jalisco', 'Buenos Aires Province',
            'Lombardia', 'North Rhine-Westphalia', 'Tamaulipas', 'Chiapas', 'Leningrad Oblast',
            'Gyeonggi-do', 'Fujian', 'Wales', 'Galicia', 'Greece Region', 'Rio de Janeiro State'
        ]),
        'ip.details.country': random_choice([
            'United States', 'Canada', 'Germany', 'France', 'United Kingdom', 'Australia',
            'Brazil', 'India', 'China', 'Japan', 'Mexico', 'Russia', 'South Africa',
            'Italy', 'Spain', 'Netherlands', 'Sweden', 'Norway', 'Denmark', 'Finland',
            'Argentina', 'Colombia', 'Chile', 'New Zealand', 'South Korea', 'Turkey',
            'Saudi Arabia', 'United Arab Emirates', 'Egypt', 'Nigeria', 'Kenya',
            'Poland', 'Portugal', 'Belgium', 'Switzerland', 'Austria', 'Ireland',
            'Czech Republic', 'Greece', 'Hungary', 'Philippines', 'Malaysia',
            'Indonesia', 'Vietnam', 'Thailand', 'Israel', 'Morocco', 'Ukraine',
            'Peru', 'Venezuela', 'Pakistan', 'Bangladesh', 'Iran', 'Iraq'
        ]),
        'ip.details.postal_code': ''.join(random.choices(string.digits, k=5)),
        'ip.details.latitude': random_latitude(),
        'ip.details.longitude': random_longitude(),
        'ip.details.timezone': random_choice([
            'UTC', 'Europe/Berlin', 'America/New_York', 'Asia/Tokyo', 'Europe/London',
            'America/Los_Angeles', 'Australia/Sydney', 'America/Chicago', 'Asia/Kolkata',
            'Europe/Moscow', 'America/Sao_Paulo', 'Africa/Johannesburg', 'Pacific/Auckland'
        ]),
        'ip.details.asn': f"AS{random_int(10000, 99999)}",
        'ip.details.organization': random_choice([
            'Google LLC', 'Microsoft Corporation', 'Apple Inc.', 'Amazon.com, Inc.',
            'Facebook, Inc.', 'IBM Corporation', 'Intel Corporation', 'Tesla, Inc.',
            'Netflix, Inc.', 'Salesforce, Inc.', 'Adobe Inc.', 'Oracle Corporation',
            'Samsung Electronics', 'Sony Corporation', 'Cisco Systems, Inc.',
            'Uber Technologies, Inc.', 'Airbnb, Inc.', 'Twitter, Inc.', 'Spotify Technology S.A.',
            'Dropbox, Inc.'
        ]),
        'ip.details.currency': random_choice([
            'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'INR', 'BRL',
            'ZAR', 'KRW', 'NZD', 'MXN', 'SGD', 'TST'
        ]),
        'ip.details.languages': random_choice([
            'en-US', 'en-GB', 'fr-FR', 'de-DE', 'es-ES', 'zh-CN', 'ja-JP', 'ko-KR',
            'pt-BR', 'ru-RU', 'it-IT', 'ar-SA', 'hi-IN', 'sv-SE', 'nl-NL'
        ]),
    }

def generate_base_dict(device_id):
    random.seed(device_id)

    base = {'ip.ip_address': '192.168.0.101',
        'ip.details.city': 'Example City',
        'ip.details.region': 'Test Region',
        'ip.details.country': 'Testland',
        'ip.details.postal_code': '12345',
        'ip.details.latitude': 52.52,
        'ip.details.longitude': 13.405,
        'ip.details.timezone': 'Europe/Berlin',
        'ip.details.asn': 'AS12345',
        'ip.details.organization': 'TestOrg Inc.',
        'ip.details.currency': 'EUR',
        'ip.details.languages': 'en,de',
        'audio.audio_hash': f"{random_int(10000, 99999)}.{random_float()}",
        'behavioral.typing_speed': None,
        'behavioral.mouse_entropy': None,
        'behavioral.url_changes.length': random_int(0, 10),
        'behavioral.time_of_visit_patterns.length': random_int(0, 10),
        'browser.browser': "Chrome 137.0",
        'browser.engine': random_choice(['Blink', 'Gecko', 'WebKit', 'Trident', 'EdgeHTML']),
        'browser.build_id': None,
        'browser.private_mode': None,
        'canvas.canvas_hash': ''.join(random.choices('abcdef0123456789', k=64)),
        'canvas.webgl_hash': ''.join(random.choices('abcdef0123456789', k=64)),
        'css_features.prefers_dark_scheme': random_bool(),
        'css_features.font_smoothing': random_bool(),
        'css_features.reduced_motion': random_bool(),
        'css_features.reduced_data': random_bool(),
        'css_features.forced_colors': random_bool(),
        'display.screen_height': random_int(720, 2160),
        'display.screen_width': random_int(1280, 3840),
        'display.color_depth': random_choice([24, 30, 32]),
        'display.device_pixel_ratio': round(random.uniform(1, 3), 2),
        'display.color_gamut': 'sRGB',
        'display.framerate': None,
        'fonts.installed_fonts.length': random_int(0, 50),
        'graphics.webgl_renderer': 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 (0x00001B80) Direct3D11 vs_5_0 ps_5_0, D3D11)',
        'graphics.webgl_vendor': 'Google Inc. (NVIDIA)',
        'graphics.webgl_extensions.length': 35,
        'graphics.webgl_extensions.0': 'ANGLE_instanced_arrays',
        'graphics.webgl_extensions.1': 'EXT_blend_minmax',
        'graphics.webgl_extensions.2': 'EXT_clip_control',
        'graphics.webgl_extensions.3': 'EXT_color_buffer_half_float',
        'graphics.webgl_extensions.4': 'EXT_depth_clamp',
        'graphics.webgl_extensions.5': 'EXT_disjoint_timer_query',
        'graphics.webgl_extensions.6': 'EXT_float_blend',
        'graphics.webgl_extensions.7': 'EXT_frag_depth',
        'graphics.webgl_extensions.8': 'EXT_polygon_offset_clamp',
        'graphics.webgl_extensions.9': 'EXT_shader_texture_lod',
        'graphics.webgl_extensions.10': 'EXT_texture_compression_bptc',
        'graphics.webgl_extensions.11': 'EXT_texture_compression_rgtc',
        'graphics.webgl_extensions.12': 'EXT_texture_filter_anisotropic',
        'graphics.webgl_extensions.13': 'EXT_texture_mirror_clamp_to_edge',
        'graphics.webgl_extensions.14': 'EXT_sRGB',
        'graphics.webgl_extensions.15': 'KHR_parallel_shader_compile',
        'graphics.webgl_extensions.16': 'OES_element_index_uint',
        'graphics.webgl_extensions.17': 'OES_fbo_render_mipmap',
        'graphics.webgl_extensions.18': 'OES_standard_derivatives',
        'graphics.webgl_extensions.19': 'OES_texture_float',
        'graphics.webgl_extensions.20': 'OES_texture_float_linear',
        'graphics.webgl_extensions.21': 'OES_texture_half_float',
        'graphics.webgl_extensions.22': 'OES_texture_half_float_linear',
        'graphics.webgl_extensions.23': 'OES_vertex_array_object',
        'graphics.webgl_extensions.24': 'WEBGL_blend_func_extended',
        'graphics.webgl_extensions.25': 'WEBGL_color_buffer_float',
        'graphics.webgl_extensions.26': 'WEBGL_compressed_texture_s3tc',
        'graphics.webgl_extensions.27': 'WEBGL_compressed_texture_s3tc_srgb',
        'graphics.webgl_extensions.28': 'WEBGL_debug_renderer_info',
        'graphics.webgl_extensions.29': 'WEBGL_debug_shaders',
        'graphics.webgl_extensions.30': 'WEBGL_depth_texture',
        'graphics.webgl_extensions.31': 'WEBGL_draw_buffers',
        'graphics.webgl_extensions.32': 'WEBGL_lose_context',
        'graphics.webgl_extensions.33': 'WEBGL_multi_draw',
        'graphics.webgl_extensions.34': 'WEBGL_polygon_mode',
        'graphics.webgpu_adapter.name': None,
        'graphics.webgpu_adapter.features.length': 12,
        'graphics.webgpu_adapter.features.0': 'float32-blendable',
        'graphics.webgpu_adapter.features.1': 'depth32float-stencil8',
        'graphics.webgpu_adapter.features.2': 'rg11b10ufloat-renderable',
        'graphics.webgpu_adapter.features.3': 'bgra8unorm-storage',
        'graphics.webgpu_adapter.features.4': 'depth-clip-control',
        'graphics.webgpu_adapter.features.5': 'texture-compression-bc',
        'graphics.webgpu_adapter.features.6': 'dual-source-blending',
        'graphics.webgpu_adapter.features.7': 'timestamp-query',
        'graphics.webgpu_adapter.features.8': 'clip-distances',
        'graphics.webgpu_adapter.features.9': 'float32-filterable',
        'graphics.webgpu_adapter.features.10': 'indirect-first-instance',
        'graphics.webgpu_adapter.features.11': 'subgroups',
        'graphics.webgpu_adapter.isFallbackAdapter': False,
        'hardware.os': 'Windows 10.0',
        'hardware.cpu_cores': random_int(2, 16),
        'hardware.device_memory': random_int(4, 64),
        'hardware.device_architecture': random_choice(['x86_64', 'arm64']),
        'http_header_fingerprint.header_count': None,
        'http_header_fingerprint.http_version': None,
        'http_header_fingerprint.tls_protocol': None,
        'http_header_fingerprint.tls_cipher_suite': None,
        'http_header_fingerprint.headers_present.length': 0,
        'http_header_fingerprint.unusual_headers.length': 0,
        'http_header_fingerprint.referer': '',
        'media.audio_codecs.length': 3,
        'media.audio_codecs.0': 'audio/mp4; codecs="mp4a.40.2"',
        'media.audio_codecs.1': 'audio/webm; codecs="opus"',
        'media.audio_codecs.2': 'audio/ogg; codecs="vorbis"',
        'media.video_codecs.length': 2,
        'media.video_codecs.0': 'video/mp4; codecs="avc1.42E01E"',
        'media.video_codecs.1': 'video/webm; codecs="vp8"',
        'media.media_devices.length': 1,
        'media.media_devices.0.deviceId': '',
        'media.media_devices.0.kind': 'audiooutput',
        'media.media_devices.0.label': '',
        'media.media_devices.0.groupId': '',
        'network.effective_type': random_choice(['4g', '3g', 'wifi']),
        'network.downlink': random_float(1, 10),
        'network.rtt': random_int(20, 300),
        'permissions.geolocation': 'prompt',
        'permissions.notifications': 'prompt',
        'permissions.camera': 'prompt',
        'permissions.microphone': 'prompt',
        'permissions.midi': 'prompt',
        'plugins.installed_plugins.length': 5,
        'plugins.installed_plugins.0': 'PDF Viewer',
        'plugins.installed_plugins.1': 'Chrome PDF Viewer',
        'plugins.installed_plugins.2': 'Chromium PDF Viewer',
        'plugins.installed_plugins.3': 'Microsoft Edge PDF Viewer',
        'plugins.installed_plugins.4': 'WebKit built-in PDF',
        'plugins.mime_types.length': 2,
        'plugins.mime_types.0': 'application/pdf',
        'plugins.mime_types.1': 'text/pdf',
        'encrypted_media_capabilities.cdm_list.length': 1,
        'encrypted_media_capabilities.cdm_list.0': 'com.widevine.alpha',
        'storage.cookies_enabled': random_bool(),
        'storage.storage_estimate.quota': random_int(1000000000, 200000000000),
        'storage.storage_estimate.usage': random_int(0, 10000),
        'storage.storage_estimate.usageDetails.indexedDB': random_int(0, 10000),
        'storage.service_workers.length': random_int(0, 5),
        'storage.indexeddb_dbs.length': 1,
        'storage.indexeddb_dbs.0': random_choice(['test', 'mainDB']),
        'storage.cache_storage_keys.length': 0,
        'time_zone.time_zone': 'Europe/Berlin',
        'time_zone.timezone_offset': 0,
        'time_zone.languages.length': 2,
        'time_zone.languages.0': 'en-US',
        'time_zone.languages.1': 'en',
        'touch_pointer.max_touch_points': random_int(0, 10),
        'touch_pointer.pointer_fine': random_bool(),
        'touch_pointer.standalone': random_bool(),
    }

    base.update(randomize_graphics_info())
    base.update(randomize_http_header_fingerprint())
    base.update(randomize_ip_details())
    base.update(random_time_zone_info())    
    base.update(randomize_indexeddb_db())
    base.update(randomize_hardware_os())
    base.update(randomize_browser_info())

    return base

def generate_data_dict(device_id):
    if device_id not in device_base_dicts:
        device_base_dicts[device_id] = generate_base_dict(device_id)
    sample = device_base_dicts[device_id]
    return sample