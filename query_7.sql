SELECT s.id AS student_id, s.name AS student_name, g.grade, g.date
        FROM students s
        JOIN grades g ON s.id = g.student_id
        JOIN subjects subj ON g.subject_id = subj.id
        JOIN groups grp ON s.group_id = grp.id
        WHERE grp.id = ? AND subj.id = ?