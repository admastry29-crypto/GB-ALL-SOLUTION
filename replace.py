import re
import os

clients = [
    ('Medanta Hospital', 'medanta.png', 'Healthcare'),
    ('Mahindra Finance', 'mahindra.png', 'Finance'),
    ('Dainik Bhaskar', 'dainik.png', 'Media'),
    ('Perfeito Ventures India', 'perfeito.png', 'Corporate'),
    ('Thyrocare', 'thyrocare.png', 'Healthcare'),
    ('IIFL Samasta', 'iifl.png', 'NBFC'),
    ('IIFL Samasta Finance', 'iifl.png', 'NBFC'), # alternate name in index
    ('Fino Payments Bank', 'fino.png', 'Banking'),
    ('Zeelab Pharmacy', 'zeelab.png', 'Healthcare'),
    ('Spandana Sphoorty', 'spandana.png', 'Microfinance'),
    ('Spandana Sphoorty Financial', 'spandana.png', 'Microfinance'), # alternate name in index
    ('State Bank of India', 'sbi.png', 'Banking'),
    ('Canara Bank', 'canara.png', 'Banking'),
    ('Birla Opus', 'birla.png', 'Retail'),
]

# For index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

for name, img, ind in clients:
    # index.html format
    # <div class="font-heading font-bold text-navy text-sm">Medanta Hospital</div>
    # <div class="text-orange text-xs mt-1">Healthcare</div>
    pattern = r'(<div class="[^"]*?text-center h-28[^"]*"[^>]*>\s*)(<div class="font-heading font-bold text-navy text-sm">)' + re.escape(name) + r'(</div>)'
    replacement = r'\1<img src="clients/' + img + r'" alt="' + name + r' Logo" class="h-12 w-auto object-contain mb-2 mx-auto" onerror="this.style.display=\'none\'">\n            \2' + name + r'\3'
    index_content = re.sub(pattern, replacement, index_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

# For clients.html
with open('clients.html', 'r', encoding='utf-8') as f:
    clients_content = f.read()

for name, img, ind in clients:
    # clients.html format
    # <div class="font-heading font-bold text-navy text-lg">Medanta Hospital</div>
    # <div class="text-orange text-sm mt-2">Healthcare</div>
    pattern = r'(<div class="[^"]*?text-center hover:shadow-lg[^"]*"[^>]*>\s*)(<div class="font-heading font-bold text-navy text-lg">)' + re.escape(name) + r'(</div>)'
    replacement = r'\1<img src="clients/' + img + r'" alt="' + name + r' Logo" class="h-16 w-auto object-contain mb-4 mx-auto" onerror="this.style.display=\'none\'">\n            \2' + name + r'\3'
    clients_content = re.sub(pattern, replacement, clients_content)

with open('clients.html', 'w', encoding='utf-8') as f:
    f.write(clients_content)

print("Done")
