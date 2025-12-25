# Data Dictionary

## Raw Dataset: online_retail.csv

| Column Name | Data Type | Description | Example Values | Missing % | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **InvoiceNo** | String | 6-digit invoice number. 'C' prefix indicates cancellation. | `536365`, `C536365` | 0% | Primary Key for transaction. |
| **StockCode** | String | 5-digit product code. | `85123A`, `22423` | 0% | Some non-standard codes (e.g., 'POST'). |
| **Description** | String | Product name. | `WHITE HANGING HEART T-LIGHT HOLDER` | ~0.2% | Dirty data (manual entry errors). |
| **Quantity** | Integer | Quantity of products per transaction. | `6`, `-12` | 0% | Negative values indicate returns. |
| **InvoiceDate** | DateTime | Timestamp of the transaction. | `2010-12-01 08:26:00` | 0% | Range: Dec 2009 - Dec 2011. |
| **UnitPrice** | Float | Price per unit in Sterling (£). | `2.55`, `4.25` | 0% | Some zero values exist (errors/gifts). |
| **CustomerID** | Float | Unique 5-digit customer number. | `17850.0` | ~25% | **Critical Issue:** High missing rate. |
| **Country** | String | Name of the country where customer resides. | `United Kingdom`, `France` | 0% | 38 unique countries. |

## Data Quality Issues Identified
1.  **Missing CustomerIDs:** Approx 25% of rows have no ID. These must be dropped for customer-level analysis.
2.  **Cancellations:** Invoices starting with 'C' must be handled/removed.
3.  **Anomalies:** Negative quantities (returns) and zero unit prices (bad data).