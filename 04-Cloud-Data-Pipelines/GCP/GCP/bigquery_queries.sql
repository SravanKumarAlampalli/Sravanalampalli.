-- Total claims per year
SELECT EXTRACT(YEAR FROM claim_date) AS year, COUNT(*) AS claims_count
FROM `healthcare.claims`
GROUP BY year
ORDER BY year;

-- Claims by provider type
SELECT provider_type, COUNT(*) AS total
FROM `healthcare.claims`
GROUP BY provider_type;
