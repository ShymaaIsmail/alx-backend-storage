-- Lists all bands with Glam rock as their main style
-- Ranked by their longevity
SELECT band_name, (2022 - COALESCE(formed, split)) AS life_span
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY life_span DESC
