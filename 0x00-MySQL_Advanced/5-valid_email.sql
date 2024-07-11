-- Trigger that resets the attribute valid_email
-- Only when the email has been changed
DELIMITER //

CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        UPDATE users
        SET valid_email = 0
        WHERE id = NEW.id;
    END IF;
END;
//

DELIMITER ;
