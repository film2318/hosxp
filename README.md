| SQL | รายละเอียด |
| :--- | :--- |
| daily.sql | ติดตามการให้บริการผู้ป่วยรายวัน |
| cost.sql | วิเคราะห์ค่าใช้จ่ายการให้บริการผู้ป่วย |
| dtx.sql | ดึงข้อมูล DTX |
| masked.sql | ปกปิดข้อมูลผู้ป่วย |
| patient.sql | แปลงและย้ายข้อมูลผู้ป่วย |
| telemedicine\.sql | ดึงข้อมูลผู้ป่วย Telemedicine |
| allergy.sql | ประวัติการแพ้ยา |
| village.sql | ข้อมูลพื้นที่และหมู่บ้านของผู้ป่วย |

## ER Diagram

```mermaid
graph TD
    ovst["ovst"]
    patient["patient"]
    vn_stat["vn_stat"]
    pttype["pttype"]
    opitemrece["opitemrece"]
    nondrugitems["nondrugitems"]
    icd101["icd101"]
    opdscreen["opdscreen"]
    dtx["DTX"]

    ovst -->|hn| patient
    ovst -->|vn| vn_stat
    ovst -->|vn| opitemrece
    ovst -->|hn| opdscreen

    vn_stat --> pttype
    vn_stat --> icd101

    opitemrece --> nondrugitems
    opdscreen -->|DTX| dtx
