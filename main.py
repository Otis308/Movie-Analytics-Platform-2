import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 1. CẤU HÌNH ĐƯỜNG DẪN HỆ THỐNG & IMPORT
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

load_dotenv(dotenv_path=project_root / ".env")

from monitoring.pipeline_tracker import PipelineLogger
from src.utils.logger import get_logger
from src.extract.tmdb_movies import pipeline as movie_pipeline, get_data_movies

logger = get_logger("Main_Orchestrator")

db_config = {
    "dbname": "neondb",
    "user": "neondb_owner",
    "password": os.getenv("DB_PASSWORD_NEON"), 
    "host": "ep-still-bread-aow0faf8.c-2.ap-southeast-1.aws.neon.tech", 
    "port": "5432",
    "sslmode": "require",
}


if __name__ == "__main__":
    logger.info("[main] KHỞI ĐỘNG HỆ THỐNG CINEFLOW")

    tracker = PipelineLogger(db_config)
    current_run_id = tracker.start_run(pipeline_name="tmdb_data_pipeline")
    logger.info(f"Đã khởi tạo phiên chạy trong DB. Run ID: {current_run_id}")
    
    try:
        logger.info("Bắt đầu kích hoạt luồng: TMDB Movies (Extract & Load)...")
        
        load_info = movie_pipeline.run(get_data_movies())

        tracker.complete_run(
            run_id=current_run_id,
            total_records=100 
        )
        logger.info("Luồng TMDB Movies hoàn tất!")
        logger.info(f"Chi tiết nạp dữ liệu:\n{load_info}")
        
    except Exception as e:
        tracker.fail_run(
            run_id=current_run_id,
            error_message=str(e)
        )
        logger.error(f"Tiến trình Pipeline chính thất bại: {e}", exc_info=True)
        
    finally:
        tracker.close()
        logger.info("Đã giải phóng kết nối Metadata Tracker.")
        logger.info("\n=======================================================================\n")