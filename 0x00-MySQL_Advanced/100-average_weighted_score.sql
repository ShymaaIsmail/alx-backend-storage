-- CREATE PROCEDURE ComputeAverageWeightedScoreForUser
-- THAT Calculates average wighted score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_score DECIMAL(10, 2);

    -- Calculate total weighted score
    SELECT SUM(score * weight) INTO total_score
    FROM scores
    WHERE user_id = user_id;

    -- Calculate total weight
    SELECT SUM(weight) INTO total_weight
    FROM scores
    WHERE user_id = user_id;

    -- Compute average weighted score
    IF total_weight > 0 THEN
        SET average_score = total_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;

    -- Insert or update the computed average score into a table or perform any desired action
    -- Example: inserting into a table `average_scores`
    INSERT INTO average_scores (user_id, average_weighted_score, computed_at)
    VALUES (user_id, average_score, NOW());

    -- You can also update an existing record if it exists for the user_id

END //

DELIMITER ;
