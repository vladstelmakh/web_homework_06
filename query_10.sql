SELECT s.name AS subject_name
        FROM subjects s
        JOIN grades g ON s.id = g.subject_id
        JOIN students stud ON g.student_id = stud.id
        JOIN teachers t ON s.teacher_id = t.id
        WHERE stud.id = ? AND t.id = ?