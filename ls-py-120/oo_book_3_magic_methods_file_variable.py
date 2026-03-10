import os

print(__file__)
print(os.path.abspath(__file__))
assets = os.path.abspath(f'{__file__}/../assets')
print(assets)

image = f'{assets}/foo.png'
print(image)