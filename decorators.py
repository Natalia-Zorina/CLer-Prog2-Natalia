#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:38:18 2021

@author: Natasha
"""
from os import path, remove
import logging
import logging.config
import functools
       
if path.isfile("logging_aufruf_funktion.log"):  
    remove("logging_aufruf_funktion.log")  

logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)  

logger_handler = logging.FileHandler("logging_aufruf_funktion.log")  
logger_handler.setLevel(logging.DEBUG)  

logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
logger_handler.setFormatter(logger_formatter) 

logger.addHandler(logger_handler)  
            
def debug(func):
    """Logging den Aufruf einer Funktion"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        logger.debug(f"Calling {func.__name__!r} function")
        value = func(*args, **kwargs)
        logger.debug(f"The function {func.__name__!r} ended")
        return value
    return wrapper_debug