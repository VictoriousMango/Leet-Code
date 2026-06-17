# Write your MySQL query statement below
select name from Customer where (referee_id is not Null and referee_id != 2) or (referee_id is Null);