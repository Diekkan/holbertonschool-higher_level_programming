-- list all shows
--
SELECT a.title, b.genre_id
FROM tv_shows a, tv_show_genres b
WHERE b.show_id = a.id
ORDER BY a.title ASC, b.genre_id ASC;
