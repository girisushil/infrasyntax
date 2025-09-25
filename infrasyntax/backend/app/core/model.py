
(This file remains the same)
from sentence_transformers import SentenceTransformer
import torch
import logging

logger = logging.getLogger(name)

class ModelLoader:
_instance = None

def __new__(cls):
    if cls._instance is None:
        cls._instance = super(ModelLoader, cls).__new__(cls)
        cls._instance.model = None
        cls._instance.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    return cls._instance

def load_model(self):
    if self.model is None:
        from .config import settings
        logger.info(f"Loading sentence-transformer model '{settings.MODEL_NAME}' onto device '{self.device}'...")
        self.model = SentenceTransformer(settings.MODEL_NAME, device=self.device)
        logger.info("✅ Model loaded successfully.")

def get_model(self):
    if self.model is None:
        self.load_model()
    return self.model
model_loader = ModelLoader()
