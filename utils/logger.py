"""
Centralized logging configuration for the AI Customer Support Agent.

This module provides a reusable logger configured with both console and
rotating file handlers. It prevents duplicate handlers, automatically
creates the log directory, and standardizes log formatting across the
application.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from utils.constants import DATE_FORMAT, LOGGER_NAME, LOG_FORMAT


def get_logger(
    name: str | None = None,
    log_directory: str | Path = "logs",
    log_file: str = "customer_support_agent.log",
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Return a configured logger.

    Parameters
    ----------
    name:
        Logger name. If omitted, the application logger name is used.
    log_directory:
        Directory where log files will be stored.
    log_file:
        Log file name.
    level:
        Logging level.

    Returns
    -------
    logging.Logger
        A configured logger instance.
    """
    logger_name = name or LOGGER_NAME
    logger = logging.getLogger(logger_name)

    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    log_dir = Path(log_directory)
    log_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT,
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        filename=log_dir / log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger