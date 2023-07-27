SELECT s.name AS subject_name
        FROM subjects s
        JOIN grades g ON s.id = g.subject_id
        JOIN students stud ON g.student_id = stud.id
        WHERE stud.id = ?