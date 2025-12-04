from app.db import get_db_status

def test_db_connection():
    status = get_db_status()
    assert status == True  # 假設 get_db_status 回傳 True 表示 DB 可以連線
