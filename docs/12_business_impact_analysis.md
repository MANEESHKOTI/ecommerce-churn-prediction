# Business Impact Analysis

## Confusion Matrix Interpretation (Test Set: 1000 Customers)
* **True Positives (Caught Churners):** 138 (Revenue Protected)
* **False Negatives (Missed Churners):** 62 (Revenue Lost)
* **False Positives (Wasted Promo):** 45 (Marketing Cost)
* **True Negatives (Loyal):** 755

## Financial Assumptions
* **Avg Customer LTV:** £500
* **Retention Campaign Cost:** £10 per customer
* **Success Rate of Campaign:** 20% (1 in 5 customers stay if targeted)

## ROI Calculation
1.  **Revenue Saved:** 138 Churners Caught * 20% Success * £500 LTV = **£13,800**
2.  **Campaign Cost:** (138 TP + 45 FP) * £10 = **£1,830**
3.  **Net Profit:** £13,800 - £1,830 = **£11,970**
4.  **ROI:** (11,970 / 1,830) * 100 = **654%**

## Recommendations
1.  **Targeting:** Focus strictly on customers with Churn Probability > 70%.
2.  **Strategy:** Offer "Free Shipping" coupons (low cost) to the "At Risk" segment identified by the model.
3.  **Ignore:** Do not spend budget on customers with Probability < 30% (High loyalty).