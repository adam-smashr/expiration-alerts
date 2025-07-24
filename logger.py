import logging
import logging.handlers
import yaml
from typing import TypedDict


class Credentials(TypedDict):
    server: str
    port: int
    from_addr: str
    to_addr: str
    username: str
    password: str


def get_credentials(file_path) -> Credentials:
    with open(file_path, "r") as f:
        yaml_cfg = yaml.load(f, Loader=yaml.FullLoader)

        return Credentials(
            server=yaml_cfg["server"],
            port=yaml_cfg["port"],
            from_addr=yaml_cfg["from_addr"],
            to_addr=yaml_cfg["to_addr"],
            username=yaml_cfg["username"],
            password=yaml_cfg["password"],
        )


# except FileNotFoundError:
#     print("Error: credential file not found")

# except yaml.YAMLError as e:
#     print(f"Error parsing YAML file: {e}")


def create_logger(creds: Credentials) -> logging.Logger:
    """build logger with email and file handling given Credential object"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("output.log", mode="w")
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    email_handler = logging.handlers.SMTPHandler(
        mailhost=(creds["server"], creds["port"]),
        fromaddr=creds["from_addr"],
        toaddrs=[creds["to_addr"]],
        subject="Freshness Report",
        credentials=(creds["username"], creds["password"]),
        secure=(),
    )
    email_handler.setLevel(logging.INFO)
    logger.addHandler(email_handler)

    return logger
