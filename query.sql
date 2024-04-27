SELECT q.quote,
    CASE
        WHEN c.name IS NULL THEN CONCAT (v.title, ' (https://vndb.org/' || q.vid || ')')
        ELSE CONCAT (
            c.name,
            ', ',
            v.title,
            ' (https://vndb.org/' || q.vid || ')'
        )
    END AS source
FROM quotes q
    JOIN vn v ON q.vid = v.id
    LEFT JOIN chars c ON q.cid = c.id