-- Creates a stored procedure ComputeAverageScoreForUser
-- That computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score  DECIMAL(5,2);
    DECLARE total_score INT;
    DECLARE corrections_count INT;
    SELECT SUM(score), COUNT(*) INTO total_score, corrections_count FROM corrections WHERE user_id = user_id;
    SET average_score = total_score / corrections_count;
    UPDATE users SET average_score = average_score WHERE user_id = user_id;
END;
//
DELIMITER ;
