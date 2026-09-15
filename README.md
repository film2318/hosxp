| SQL | รายละเอียด |
| :--- | :--- |
| `check_daily_patient.sql` | ติดตามการให้บริการผู้ป่วยรายวัน |
| `check_service_cost.sql` | วิเคราะห์ค่าใช้จ่ายการให้บริการผู้ป่วย |
| `dtx_export.sql` | ดึงข้อมูล DTX |
| `masked_patient.sql` | ปกปิดข้อมูลผู้ป่วย |
| `migration_patient_data.sql` | แปลงและย้ายข้อมูลผู้ป่วย |
| `telemedicine_export.sql` | ดึงข้อมูลผู้ป่วย Telemedicine |
| `view_allergy_history.sql` | ประวัติการแพ้ยา |
| `view_village.sql` | ข้อมูลพื้นที่และหมู่บ้านของผู้ป่วย |

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
