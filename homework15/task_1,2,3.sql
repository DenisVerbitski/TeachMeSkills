
#Сколько всего байт «занимают» песни из таблицы tracks
SELECT SUM(Bytes) FROM tracks;

#Сколько записей находится в таблицах employees
SELECT COUNT(CustomerId) FROM customers;

#Сколько записей находится в таблицах customers
SELECT COUNT(EmployeeId) FROM employees;

#Получить список треков tracks из альбома «A-Sides»
SELECT Title, name
FROM albums 
INNER JOIN tracks 
ON albums.AlbumId = tracks.AlbumId
WHERE Title = "A-Sides";
