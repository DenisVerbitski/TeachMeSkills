SELECT Title, albumPrice 
FROM albums
INNER JOIN (
	SELECT SUM(UnitPrice) as albumPrice, Albumid
	FROM tracks
	GROUP BY Albumid
	)
USING (Albumid)

