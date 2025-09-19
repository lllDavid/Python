import torch
import torch.nn as nn

import csv
def load_vocab_from_csv(filename):
    vocab = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  
                vocab.append(row[0])  
    return vocab

ip_city_vocab = load_vocab_from_csv('csv/cities.csv')
ip_region_vocab = load_vocab_from_csv('csv/regions.csv')
ip_country_vocab = load_vocab_from_csv('csv/countries.csv')
ip_timezone_vocab = load_vocab_from_csv('csv/timezones.csv')
ip_organization_vocab = load_vocab_from_csv('csv/isps.csv')
ip_currency_vocab = load_vocab_from_csv('csv/currencies.csv')
ip_languages_vocab = load_vocab_from_csv('csv/languages.csv')
ip_asn_vocab = load_vocab_from_csv('csv/asn.csv')
timezone_languages_vocab = ip_languages_vocab 
timezone_vocab = ip_timezone_vocab

class CategoricalEmbedder:
    def __init__(self, vocab, embedding_dim, multi_valued=False):
        self.vocab = vocab
        self.multi_valued = multi_valued
        self.embedding = nn.Embedding(len(vocab), embedding_dim)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.embedding = self.embedding.to(self.device)
        self.index_map = {val: i for i, val in enumerate(vocab)}
        self.embedding_dim = embedding_dim

    def __call__(self, values):
        if not isinstance(values, list):
            values = [values]
        indices = [self.index_map.get(v, len(self.vocab) - 1) for v in values if v in self.index_map]
        if not indices:
            return torch.zeros(1, self.embedding_dim, device=self.device)
        indices_tensor = torch.tensor(indices, device=self.device)
        embedded = self.embedding(indices_tensor)
        return embedded.mean(dim=0, keepdim=True) if self.multi_valued else embedded

embedding_dim = 128

# IP Address
city_embedder = CategoricalEmbedder(ip_city_vocab, embedding_dim, multi_valued=False)
region_embedder = CategoricalEmbedder(ip_region_vocab, embedding_dim, multi_valued=False)
country_embedder = CategoricalEmbedder(ip_country_vocab, embedding_dim, multi_valued=False)
timezone_embedder = CategoricalEmbedder(ip_timezone_vocab, embedding_dim, multi_valued=False)
organization_embedder = CategoricalEmbedder(ip_organization_vocab, embedding_dim, multi_valued=False)
currency_embedder = CategoricalEmbedder(ip_currency_vocab, embedding_dim, multi_valued=False)
languages_embedder = CategoricalEmbedder(ip_languages_vocab, embedding_dim, multi_valued=False)
asn_embedder = CategoricalEmbedder(ip_asn_vocab, embedding_dim, multi_valued=False)


# Browser
browser_browser_vocab = ['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', 'Vivaldi', 'Tor Browser', 'Internet Explorer', 'Brave', 'Unknown']
browser_engine_vocab = ['Blink', 'Gecko', 'WebKit', 'Trident', 'EdgeHTML', 'Presto', 'Goanna', 'KHTML', 'Servo', 'Flow', 'NetSurf', 'WebView']

# Canvas
canvas_hash_vocab = ['abcdef0123456789' * 16, 'Unknown']  
webgl_hash_vocab = ['abcdef0123456789' * 16, 'Unknown']  

# Display
color_gamut_vocab = ['sRGB', 'P3', 'Rec2020', 'Unknown']

# Graphics
webgl_renderer_vocab = [
    'ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 (0x00001B80) Direct3D11 vs_5_0 ps_5_0, D3D11)',   'ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 (0x2503) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (NVIDIA, NVIDIA GeForce RTX 3070 (0x2484) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 (0x2206) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (NVIDIA, NVIDIA GeForce RTX 3090 (0x2204) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Ti (0x2782) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 (0x2684) Direct3D11 vs_5_0 ps_5_0, D3D11)','ANGLE (AMD, AMD Radeon RX 6600 XT (0x73FF) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (AMD, AMD Radeon RX 6700 XT (0x73BF) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (AMD, AMD Radeon RX 6800 (0x73BF) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (AMD, AMD Radeon RX 7900 XTX (0x744C) Direct3D11 vs_5_0 ps_5_0, D3D11)','ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'ANGLE (Intel, Intel(R) Arc(TM) A770 Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)',  'ANGLE (Apple, Apple M1, Metal)',
    'ANGLE (Apple, Apple M1 Pro, Metal)',
    'ANGLE (Apple, Apple M2, Metal)',
    'ANGLE (Apple, Apple M3 Max, Metal)',  'ANGLE (Apple, Apple M1, Metal)',
    'ANGLE (Apple, Apple M1 Pro, Metal)',
    'ANGLE (Apple, Apple M2, Metal)',
    'ANGLE (Apple, Apple M3 Max, Metal)',
    'Unknown'
]
webgl_vendor_vocab = ['Google Inc. (NVIDIA)',   'Google Inc. (NVIDIA)',
    'Google Inc. (AMD)',
    'Google Inc. (Intel)',
    'Google Inc. (Apple)',
    'Google Inc. (Qualcomm)',
    'Google Inc. (ARM)',
    'Google Inc. (Imagination Technologies)',  
    'Google Inc. (Broadcom)',                 
    'Google Inc. (Microsoft Corporation)',   
    'Apple Inc.',
    'Mozilla (Intel)',
    'Mozilla (NVIDIA)',
    'ANGLE (Intel)',
    'ANGLE (NVIDIA)',
    'ANGLE (AMD)','Unknown']

webgl_extensions_vocab = [
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
webgpu_features_vocab = [
    'float32-blendable', 'depth32float-stencil8', 'rg11b10ufloat-renderable',
    'bgra8unorm-storage', 'depth-clip-control', 'texture-compression-bc',
    'dual-source-blending', 'timestamp-query', 'clip-distances',
    'float32-filterable', 'indirect-first-instance', 'subgroups'
]

# Media Audio
audio_codecs_vocab = [
    'audio/mp4; codecs="mp4a.40.2"', 'audio/webm; codecs="opus"',
    'audio/ogg; codecs="vorbis"', 'Unknown'
]
video_codecs_vocab = [
    'video/mp4; codecs="avc1.42E01E"', 'video/webm; codecs="vp8"', 'Unknown'
]

media_devices_kind_vocab = ['audiooutput', 'audioinput', 'videoinput', 'Unknown']

# Hardware
device_architecture_vocab = ['x86_64', 'arm64', 'Unknown']

# Permissions
permissions_vocab = ['prompt', 'granted', 'denied', 'Unknown']

# Plugins
plugins_vocab = [
    'PDF Viewer', 'Chrome PDF Viewer', 'Chromium PDF Viewer',
    'Microsoft Edge PDF Viewer', 'WebKit built-in PDF', 'Unknown'
]
mime_types_vocab = ['application/pdf', 'text/pdf', 'Unknown']

# Encrypted Media Capabilities
cdm_list_vocab = ['com.widevine.alpha', 'Unknown']

# Storage
indexeddb_dbs_vocab = [
    'test',
    'mainDB',
    'firebaseLocalStorageDb',
    'firebase-database',
    'firebase-installations-database',
    'workbox-expiration',
    'workbox-cache-db',
    'idb-keyval-store',
    'localforage',
    'offline-db',
    'pouchdb',
    'appDB',
    'user-data',
    'session-store',
    'sw-cache',
    'dexie-db',
    'notion-user-data',
    'github-db',
    'reddit-storage',
    'drive-client-database',
    'dropbox-auth',
    'playback-cache',
    'shopping-cart',
    'client-settings',
    'tracking-events',
    'google-analytics-db',
    'cookie-consent-db',
    'Unknown'
]

# Define sample values from the provided data
data = {
    'ip.details.city': 'Example City',
    'ip.details.region': 'Test Region',
    'ip.details.country': 'Testland',
    'ip.details.timezone': 'Europe/Berlin',
    'ip.details.organization': 'TestOrg Inc.',
    'ip.details.currency': 'EUR',
    'ip.details.languages': ['en', 'de'],
    'browser.browser': 'Chrome 137.0',
    'browser.engine': 'Blink',  
    'canvas.canvas_hash': 'abcdef0123456789' * 16,  
    'canvas.webgl_hash': 'abcdef0123456789' * 16,  
    'display.color_gamut': 'sRGB',
    'graphics.webgl_renderer': 'ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 (0x00001B80) Direct3D11 vs_5_0 ps_5_0, D3D11)',
    'graphics.webgl_vendor': 'Google Inc. (NVIDIA)',
    'graphics.webgl_extensions': webgl_extensions_vocab,  
    'graphics.webgpu_adapter.features': webgpu_features_vocab,  
    'media.audio_codecs': [
        'audio/mp4; codecs="mp4a.40.2"',
        'audio/webm; codecs="opus"',
        'audio/ogg; codecs="vorbis"'
    ],
    'media.video_codecs': [
        'video/mp4; codecs="avc1.42E01E"',
        'video/webm; codecs="vp8"'
    ],
    'media.media_devices.kind': 'audiooutput',
    'hardware.device_architecture': 'x86_64',  
    'permissions.geolocation': 'prompt',
    'permissions.notifications': 'prompt',
    'permissions.camera': 'prompt',
    'permissions.microphone': 'prompt',
    'permissions.midi': 'prompt',
    'plugins.installed_plugins': [
        'PDF Viewer', 'Chrome PDF Viewer', 'Chromium PDF Viewer',
        'Microsoft Edge PDF Viewer', 'WebKit built-in PDF'
    ],
    'plugins.mime_types': ['application/pdf', 'text/pdf'],
    'encrypted_media_capabilities.cdm_list': ['com.widevine.alpha'],
    'storage.indexeddb_dbs': ['maindb'], 
    'time_zone.time_zone': 'Europe/Berlin',
    'time_zone.languages': ['en-US', 'en']
}

# Generate embeddings for each feature
embeddings = {}

# Define features and vocab (multi_valued = True or False)
features = [
    ('ip.details.city', ip_city_vocab, False),
    ('ip.details.region', ip_region_vocab, False),
    ('ip.details.country', ip_country_vocab, False),
    ('ip.details.timezone', ip_timezone_vocab, False),
    ('ip.details.organization', ip_organization_vocab, False),
    ('ip.details.currency', ip_currency_vocab, False),
    ('browser.browser', browser_browser_vocab, False),
    ('browser.engine', browser_engine_vocab, False),
    ('canvas.canvas_hash', canvas_hash_vocab, False),
    ('canvas.webgl_hash', webgl_hash_vocab, False),
    ('display.color_gamut', color_gamut_vocab, False),
    ('graphics.webgl_renderer', webgl_renderer_vocab, False),
    ('graphics.webgl_vendor', webgl_vendor_vocab, False),
    ('media.media_devices.kind', media_devices_kind_vocab, False),
    ('hardware.device_architecture', device_architecture_vocab, False),
    ('permissions.geolocation', permissions_vocab, False),
    ('permissions.notifications', permissions_vocab, False),
    ('permissions.camera', permissions_vocab, False),
    ('permissions.microphone', permissions_vocab, False),
    ('permissions.midi', permissions_vocab, False),
    ('time_zone.time_zone', timezone_vocab, False),
    ('ip.details.languages', ip_languages_vocab, True),
    ('graphics.webgl_extensions', webgl_extensions_vocab, True),
    ('graphics.webgpu_adapter.features', webgpu_features_vocab, True),
    ('media.audio_codecs', audio_codecs_vocab, True),
    ('media.video_codecs', video_codecs_vocab, True),
    ('plugins.installed_plugins', plugins_vocab, True),
    ('plugins.mime_types', mime_types_vocab, True),
    ('encrypted_media_capabilities.cdm_list', cdm_list_vocab, True),
    ('storage.indexeddb_dbs', indexeddb_dbs_vocab, True),
    ('time_zone.languages', timezone_languages_vocab, True)
]

for feature, vocab, is_multi in features:
    embedder = CategoricalEmbedder(vocab, embedding_dim, multi_valued=is_multi)
    values = data.get(feature, 'Unknown') if not is_multi else data.get(feature, ['Unknown'])
    embeddings[feature] = embedder(values)
    print(f"{feature} embedding shape: {embeddings[feature].shape}")


# Example: Print one embedding vector to show values
print("\nExample embedding for browser.engine:")
print(embeddings['browser.engine'])

print("Shape of ip.details.timezone:", embeddings['ip.details.timezone'].shape)
print("Shape of canvas.canvas_hash:", embeddings['canvas.canvas_hash'].shape)


def normalize_to_tensor(value, min_val, max_val, embedding_dim=8, device='cuda' if torch.cuda.is_available() else 'cpu'):
    """
    Normalize a numerical value to [0, 1] and convert to a [1, 8] tensor.
    
    Args:
        value: The numerical value to normalize (int or float).
        min_val: Minimum value of the feature's range.
        max_val: Maximum value of the feature's range.
        embedding_dim: Target dimension for the tensor (default: 8).
        device: Device for the tensor ('cuda' or 'cpu').
    
    Returns:
        torch.Tensor: A [1, 8] tensor with the normalized value repeated.
    """
    # Handle None or invalid values
    if value is None or not isinstance(value, (int, float)):
        return torch.zeros(1, embedding_dim, device=device)
    
    # Ensure value is within bounds
    value = max(min_val, min(max_val, value))
    
    # Min-Max normalization
    normalized = (value - min_val) / (max_val - min_val) if max_val != min_val else 0.5
    
    # Create [1, 8] tensor by repeating the normalized value
    tensor = torch.full((1, embedding_dim), normalized, device=device)
    return tensor

# Define ranges for numerical features
numerical_features = {
    'ip.details.latitude': {'min': -90, 'max': 90},
    'ip.details.longitude': {'min': -180, 'max': 180},
    'behavioral.url_changes.length': {'min': 0, 'max': 10},
    'behavioral.time_of_visit_patterns.length': {'min': 0, 'max': 10},
    'display.screen_height': {'min': 720, 'max': 2160},
    'display.screen_width': {'min': 1280, 'max': 3840},
    'display.device_pixel_ratio': {'min': 1, 'max': 3},
    'fonts.installed_fonts.length': {'min': 0, 'max': 50},
    'hardware.cpu_cores': {'min': 2, 'max': 16},
    'hardware.device_memory': {'min': 4, 'max': 64},
    'network.downlink': {'min': 1, 'max': 10},
    'network.rtt': {'min': 20, 'max': 300},
    'storage.storage_estimate.quota': {'min': 1000000000, 'max': 200000000000},
    'storage.storage_estimate.usage': {'min': 0, 'max': 10000},
    'storage.storage_estimate.usageDetails.indexedDB': {'min': 0, 'max': 10000},
    'time_zone.timezone_offset': {'min': -720, 'max': 720}
}

# Example data (from base dictionary)
base = {
    'ip.details.latitude': 52.52,
    'ip.details.longitude': 13.405,
    'behavioral.url_changes.length': 5,
    'behavioral.time_of_visit_patterns.length': 3,
    'display.screen_height': 1080,
    'display.screen_width': 1920,
    'display.device_pixel_ratio': 1.5,
    'fonts.installed_fonts.length': 30,
    'hardware.cpu_cores': 8,
    'hardware.device_memory': 16,
    'network.downlink': 5.5,
    'network.rtt': 100,
    'storage.storage_estimate.quota': 50000000000,
    'storage.storage_estimate.usage': 5000,
    'storage.storage_estimate.usageDetails.indexedDB': 2000,
    'time_zone.timezone_offset': 0
}

# Generate normalized [1, 8] tensors for numerical features
embeddings = {}
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

for feature, range_info in numerical_features.items():
    value = base.get(feature, 0)  # Default to 0 if missing
    tensor = normalize_to_tensor(
        value=value,
        min_val=range_info['min'],
        max_val=range_info['max'],
        embedding_dim=8,
        device=device
    )
    embeddings[feature] = tensor
    print(f"{feature} normalized tensor shape: {tensor.shape}")
    print(f"{feature} normalized tensor: {tensor}")

# Example output for one feature
print("\nExample normalized tensor for ip.details.latitude:")
print(embeddings['ip.details.latitude'].shape)

def encode_sample(data_dict):
    categorical_embeddings = {}
    for feature, vocab, is_multi in features:
        embedder = CategoricalEmbedder(vocab, embedding_dim=8, multi_valued=is_multi)
        values = data_dict.get(feature, 'Unknown') if not is_multi else data_dict.get(feature, ['Unknown'])
        categorical_embeddings[feature] = embedder(values)
    
    numerical_embeddings = {}
    for feature, range_info in numerical_features.items():
        value = data_dict.get(feature, 0)
        tensor = normalize_to_tensor(value, range_info['min'], range_info['max'], embedding_dim=8)
        numerical_embeddings[feature] = tensor
    
    combined = torch.cat(list(categorical_embeddings.values()) + list(numerical_embeddings.values()), dim=0)  # [47, 8]
    return combined.view(-1)  # [376]