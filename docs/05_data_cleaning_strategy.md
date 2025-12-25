# Data Cleaning Strategy

## 1. Missing Values Strategy
* **CustomerID (~25% Missing):**
    * **Decision:** **DROP**.
    * **Reasoning:** We cannot build a customer-level history without a unique identifier. Imputing CustomerID is impossible and risky.
    * **Impact:** We expect to lose approximately 25% of the raw rows.
* **Description:**
    * **Decision:** Fill with "Unknown" or Drop if row is also missing CustomerID.

## 2. Handling Cancellations
* **Identifier:** `InvoiceNo` starts with 'C'.
* **Decision:** **REMOVE**.
* **Reasoning:** Cancellations/Returns represent negative behavior that complicates the definition of "purchase activity." For this churn model, we focus on valid, completed sales.

## 3. Negative Quantities & Prices
* **Negative Quantity:** Usually indicates returns. **REMOVE**.
* **Zero/Negative Prices:** Indicates errors or bad debt adjustments. **REMOVE**.

## 4. Outlier Detection
* **Method:** Interquartile Range (IQR).
* **Threshold:** Remove data points outside $Q1 - 1.5 * IQR$ and $Q3 + 1.5 * IQR$.
* **Focus:** primarily on `Quantity` and `UnitPrice` to prevent massive bulk orders (wholesalers) from skewing the model, as we are targeting standard retail behavior.

## 5. Duplicate Handling
* **Strategy:** Drop full duplicates where `InvoiceNo`, `StockCode`, `Quantity`, and `InvoiceDate` are identical.

## 6. Data Type Conversions
* **InvoiceDate:** Convert string to `datetime` objects.
* **CustomerID:** Convert float to `integer` (e.g., 12345.0 -> 12345).
* **Categorical:** `Country` will be analyzed but likely dropped or grouped due to high cardinality.