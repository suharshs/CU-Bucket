

-- find activities not in the user's bucket
SELECT DISTINCT a.ID AS 'activityID', a.name, c.name AS 'category'
FROM Activity a
LEFT JOIN UserInterest ui
	ON a.ID = ui.activityID
JOIN Category c
	ON a.ID = c.activityID
WHERE ui.userName IS NULL OR ui.userName != 'martin'


-- find user's most frequently bucketed categories
SELECT COUNT(a.name) AS 'activities', c.name AS 'category'
FROM Activity a
JOIN Category c
	ON a.ID = c.activityID
WHERE a.creator = 'martin'
GROUP BY c.name
ORDER BY activities DESC
LIMIT 5    -- This can change, only the top 5 for now





-- First attempt: this just selects anything that matches a single 'like' of the user
-- find activities not in the user's bucket
SELECT DISTINCT a.ID AS 'activityID', a.name, c.name AS 'category'
FROM Activity a
LEFT JOIN UserInterest ui
	ON a.ID = ui.activityID
JOIN Category c
	ON a.ID = c.activityID
WHERE ui.userName IS NULL OR ui.userName != 'martin'
AND c.name IN (
-- find user's most frequently bucketed categories
SELECT c.name
FROM Activity a
JOIN Category c
	ON a.ID = c.activityID
WHERE a.creator = 'martin'
GROUP BY c.name
ORDER BY COUNT(a.name) DESC
);





-- This works! Selects in descending order by number of categories matched
SELECT DISTINCT c.activityID AS 'ID', a.name, a.description, a.creator, a.rating, a.location
FROM 
(SELECT c.name, COUNT(c.activityID) AS 'activities'
 FROM UserInterest ui
JOIN Activity a
ON a.ID = ui.activityID
JOIN Category c
ON a.ID = c.activityID
WHERE ui.userName = 'martin'
GROUP BY c.name
ORDER BY Count(c.activityID) DESC) bucket

JOIN Category c
ON c.name = bucket.name

JOIN Activity a 
ON a.ID = c.activityID

LEFT JOIN UserInterest ui
ON a.ID = ui.activityID

WHERE ui.userName IS NULL 
OR ui.userName != 'martin'



