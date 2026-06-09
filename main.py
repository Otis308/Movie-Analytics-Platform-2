import os
import sys
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

load_dotenv(dotenv_path=project_root / ".env")
from src.utils.logger import get_logger
from src.extract.tmdb_movies import pipeline as movie_pipeline, get_data_movies

# Khởi tạo logger trung tâm cho file Main
logger = get_logger("Main_Orchestrator")

if __name__ == "__main__":
    logger.info("[MAIN] KHỞI ĐỘNG HỆ THỐNG CINEFLOW")
    
    try:
        # Chạy luồng Extract & Load
        logger.info("Bắt đầu kích hoạt luồng: TMDB Movies (Extract & Load)...")
        
        load_info = movie_pipeline.run(get_data_movies())
        
        # Ghi log kết quả chi tiết từ dlt trả về
        logger.info(f"Luồng TMDB Movies hoàn tất xuất sắc!\n{load_info}")
        
    except Exception as e:
        logger.error(f"Tiến trình Pipeline chính thất bại: {e}", exc_info=True)
    finally:
        logger.info("\n===============================================================================================================================================================================\n")