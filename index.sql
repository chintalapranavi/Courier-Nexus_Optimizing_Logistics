-- 1. Unique Index on Tracking Number (Shipments Table)
CREATE UNIQUE INDEX idx_tracking_number
ON Shipments(tracking_number);

-- 2. Non-clustered Index on Status (Shipments Table)
CREATE INDEX idx_shipment_status
ON Shipments(status);

-- 3. Non-clustered Index on Receiver ID (Shipments Table)
CREATE INDEX idx_receiver_id
ON Shipments(receiver_id);

-- 4. Non-clustered Index on Claim Status (Claims Table)
CREATE INDEX idx_claim_status
ON Claims(claim_status);

-- 5. Non-clustered Index on Feedback Date (Customer Feedback Table)
CREATE INDEX idx_feedback_date
ON CustomerFeedback(feedback_date);

-- 6. Non-clustered Index on Attempt Date (Delivery Attempts Table)
CREATE INDEX idx_attempt_date
ON DeliveryAttempts(attempt_date);