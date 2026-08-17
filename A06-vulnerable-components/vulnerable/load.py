import yaml
# BUG: old PyYAML's default yaml.load() can construct arbitrary Python objects
data = yaml.load(open("config.yml"))
print("Loaded:", data)
