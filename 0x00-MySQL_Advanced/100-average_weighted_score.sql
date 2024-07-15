-- Define the procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_score DECIMAL(10, 2);

    -- Calculate total weighted score
    SELECT SUM(score * weight) INTO total_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate total weight
    SELECT SUM(weight) INTO total_weight
    FROM projects
    JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;

    -- Compute average weighted score
    IF total_weight > 0 THEN
        SET average_score = total_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;
    
    -- Update the average_score in users table for the given user_id
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;

END //

DELIMITER ;
