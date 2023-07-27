SELECT t.id AS teacher_id, t.name AS teacher_name, AVG(g.grade) AS avg_grade
        FROM teachers t
        JOIN subjects s ON t.id = s.teacher_id
        JOIN grades g ON s.id = g.subject_id
        GROUP BY t.id, t.name
        HAVING teacher_id = ?