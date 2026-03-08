USE iss;

SELECT l.location_id, l.timestamp, l.latitude, l.longitude, r.reporter_name AS reporter
FROM locations l
JOIN reporters r ON l.reporter_id = r.reporter_id;
