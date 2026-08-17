import yaml
# THE FIX: safe_load CANNOT build arbitrary Python objects
data = yaml.safe_load(open("config.yml"))
print("Loaded:", data)
