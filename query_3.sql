SELECT grp.name AS group_name, AVG(g.grade) AS avg_grade
        FROM groups grp
        LEFT JOIN students s ON grp.id = s.group_id
        LEFT JOIN grades g ON s.id = g.student_id
        WHERE g.subject_id = ?
        GROUP BY grp.id, grp.name