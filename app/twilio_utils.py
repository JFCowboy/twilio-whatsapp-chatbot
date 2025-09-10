# Standard library import
import logging

# Third-party imports
from twilio.rest import Client
from decouple import config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(to_number, body_text):
    pass