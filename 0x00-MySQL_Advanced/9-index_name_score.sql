-- CREATE INDEX idx_name_first_score
-- ON TWO COLUMNS
CREATE INDEX idx_name_first_score ON names (name(1), score);
