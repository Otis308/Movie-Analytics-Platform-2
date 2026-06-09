import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

def get_logger(module_name):

    # 1. Định nghĩa thư mục chứa log ở thư mục gốc dự án
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = Path(__file__).resolve().parents[2]

    log_dir = os.path.join(project_root, "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "pipeline.log")

    # 2. Khởi tạo Logger
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO) # Ghi lại từ mức INFO trở lên (INFO, WARNING, ERROR, CRITICAL)

    # Tránh tình trạng log bị nhân đôi khi gọi nhiều lần
    if not logger.handlers:
        # 3. Format log
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # 4. Ghi ra Terminal (Console Handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 5. Ghi vào File (File Handler) - Tự động cắt file nếu dung lượng quá 5MB
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
    