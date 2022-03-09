-- lists all shows
--
SELECT a.title, c.name
FROM tv_shows a
LEFT JOIN tv_show_genres b
ON a.id = b.show_id
LEFT JOIN tv_genres c
ON b.genre_id = c.id
ORDER BY a.title ASC, c.name ASC;
