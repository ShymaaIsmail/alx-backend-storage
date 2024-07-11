-- Trigger that decreases the quantity of an item
-- After adding a new order.
DELIMITER //
CREATE TRIGGER decrease_quantity After INSERT ON orders
FOR EACH ROW    
BEGIN  
    UPDATE items
    SET quantity = quantity - NEW.number 
    WHERE items.name = NEW.item_name;
END;

//
DELIMITER ;
