import yaml
import os

def read_yaml(file_path: str = "config/pipeline_config.yaml") -> dict:
    """
    Loads YAML configuration.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at {file_path}")
    
    with open(file_path,"r") as yaml_file:
        config = yaml.safe_load(yaml_file)
        return config