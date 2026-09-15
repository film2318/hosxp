| SQL | Purpose |
| :--- | :--- |
| `check_daily_patient.sql` | Daily patient service tracking |
| `check_service_cost.sql` | Patient service cost analysis |
| `dtx_export.sql` | DTX data extraction |
| `masked_patient.sql` | Patient data masking |
| `migration_patient_data.sql` | Patient data transformation and migration |
| `telemedicine_export.sql` | Telemedicine patient data extraction |
| `view_allergy_history.sql` | Drug allergy history |
| `view_village.sql` | Patient geographic information |

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
