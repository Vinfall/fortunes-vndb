SELECT
    q.quote,
    CASE
        WHEN c.name IS null THEN concat(v.title, ' (https://vndb.org/' || q.vid || ')')
        ELSE concat(
            c.name,
            ', ',
            v.title,
            ' (https://vndb.org/' || q.vid || ')'
        )
    END AS source
FROM quotes AS q
INNER JOIN vn AS v ON q.vid = v.id
LEFT JOIN chars AS c ON q.cid = c.id