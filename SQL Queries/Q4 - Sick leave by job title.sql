SELECT JobTitle, avg(SickLeaveHours) AS Average_SickLeave, OrganizationLevel
FROM HumanResources.Employee
GROUP BY jobtitle, OrganizationLevel
ORDER BY OrganizationLevel