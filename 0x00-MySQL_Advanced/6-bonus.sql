-- Create a stored procedure AddBonus
-- That adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    SET project_id = (SELECT id FROM projects WHERE name = project_name);
    IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name);
    SET project_id = LAST_INSERT_ID();
    END IF;
    
    SET user_id = (SELECT id FROM users WHERE id = user_id);
    IF user_id IS NOT NULL
    THEN
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
    END IF;
END;
//

DELIMITER ;
