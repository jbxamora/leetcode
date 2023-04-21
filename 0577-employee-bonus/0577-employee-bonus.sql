select name,bonus from employee
left join bonus using (empId)
where coalesce(bonus,0)<1000