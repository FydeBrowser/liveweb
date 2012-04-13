"""Liveweb configuration.

This is initialized by calling the load(configfile) function on startup.
"""
import yaml
import os
import redis
import logging

storage_root = "/tmp/records"
user_agent = "ia_archiver(OS-Wayback)"

M = 1024 * 1024

# Max size of ARC record that can be stored in cache
max_cacheable_size = 10 * M

expire_time = 3600

redis_params = {}

_redis_client = None

def get_redis_client():
    """Returns the redis client instance created from the config.
    """
    # TODO: this is not right place to have this function. Move it to some better place.
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.StrictRedis(**redis_params)
    return _redis_client

def load(filename):
    """Loads configuration from specified config file.
    """
    logging.info("Loading config file: %s", filename)
    if not os.path.exists(filename):
        logging.warn("config file not found: %s, ignoring...", filename)
        return
        
    d = yaml.safe_load(filename)
    globals().update(d)
    
    if not os.path.exists(storage_root):
        os.makedirs(storage_root)
    
# handy function to check for existance of a config parameter
get = globals().get
