import yaml
import logging

from dataclasses import dataclass
from smtplib import SMTP
from email.message import EmailMessage

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    # filename="myapp.log",
    # filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@dataclass
class AppConfig:
    server: str
    port: int
    from_addr: str
    to_addr: str
    username: str
    password: str
    subject: str


def get_app_config(file_path) -> AppConfig:
    with open(file_path, "r") as f:
        try:
            yaml_cfg: dict[str, str | int] = yaml.load(f, Loader=yaml.SafeLoader)
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")

        REQUIRED_KEYS = [
            "server",
            "port",
            "from_addr",
            "to_addr",
            "username",
            "password",
            "subject",
        ]

        # validate keys, raise an error if any are missing
        keys: dict[str, bool] = {key: key in yaml_cfg for key in REQUIRED_KEYS}
        logger.debug(keys)

        if not all(keys.values()):
            raise KeyError(
                f"Missing required Keys: {[key for key in keys if not keys[key]]}"
            )

        return AppConfig(
            server=str(yaml_cfg["server"]),
            port=int(yaml_cfg["port"]),
            from_addr=str(yaml_cfg["from_addr"]),
            to_addr=str(yaml_cfg["to_addr"]),
            username=str(yaml_cfg["username"]),
            password=str(yaml_cfg["password"]),
            subject=str(yaml_cfg["subject"]),
        )


def setup_server(cfg: AppConfig) -> SMTP:
    logger.debug("connecting to server...")
    s = SMTP(cfg.server)
    s.starttls()
    s.login(cfg.username, cfg.password)

    return s


def format_message(cfg: AppConfig, content: str) -> EmailMessage:
    email = EmailMessage()
    email.set_content(content)
    email["Subject"] = cfg.subject
    email["From"] = cfg.from_addr
    email["To"] = cfg.to_addr

    return email


def send_email(cfg: AppConfig) -> None:
    logger.debug("preparing email...")
    message = format_message(cfg, content="hello")
    server = setup_server(cfg)

    logger.debug("sending message...")
    server.send_message(message)

    logger.debug("success!")
    server.quit()


if __name__ == "__main__":
    cfg = get_app_config("credentials.yaml")
    send_email(cfg=cfg)
