import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger():
"""Sets up a centralized logger."""
log_formatter = logging.Formatter(
'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# File handler
file_handler = RotatingFileHandler(
    'infrasyntax.log', maxBytes=5*1024*1024, backupCount=2
)
file_handler.setFormatter(log_formatter)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)

# Get root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Clear existing handlers
if logger.hasHandlers():
    logger.handlers.clear()
    
logger.addHandler(file_handler)
logger.addHandler(console_handler)

return logger
logger = setup_logger()
