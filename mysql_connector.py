
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import warnings

# 1. ปิดคำเตือน
warnings.filterwarnings('ignore')

# 2. ตั้งค่าการแสดงผล
pd.set_option('display.max_colwidth', 20)

# 3. เชื่อมต่อฐานข้อมูล MySQL: hosxp
connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="yourpassword",
    host="yourusername",
    port=3306,
    database="mydatabase"
)

engine = create_engine(connection_url)

try:
    query = "SELECT * FROM ovst "
    df = pd.read_sql(query, engine)

    # 4. เลือกเฉพาะคอลัมน์ที่ต้องการแสดง
    columns_to_show = [
        'hn',
        'vstdate',
        'vatime',
        'pname'
    ]

    existing_cols = [
        col for col in columns_to_show
        if col in df.columns
    ]

    filtered_df = df[existing_cols]


    print(
        filtered_df.to_markdown(
            index=False,
            tablefmt="grid"
        )
    )

except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
    print(
        "หากไม่มีไลบรารี tabulate ให้ติดตั้งด้วยคำสั่ง: "
        "pip install tabulate"
    )

finally:
    engine.dispose()
