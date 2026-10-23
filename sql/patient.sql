SELECT
    case
    when p.sex = 1  then '003'
    when p.sex = 2 then '004'
  end as pname,
    REGEXP_REPLACE(p.fname, '\\s*\\(.*\\)$', '') AS fname,
    REGEXP_REPLACE(p.lname, '\\s*\\(.*\\)$', '') AS lname,
    p.sex,
    LPAD(DAY(p.birthday), 2, '0') AS day_2digit,
    LPAD(MONTH(p.birthday), 2, '0') AS month_2digit,
    YEAR(p.birthday) AS year,
    p.cid,
    CASE
    WHEN p.type_area IN ('1', '2', '3', '4') THEN p.type_area
    ELSE '0'
END AS type_area,
    vl.village_code,
    vl.village_name,
    REGEXP_SUBSTR(p.addrpart, '[0-9]+(/[0-9]+)?') AS house_number,
    p.road
FROM 
    patient p
LEFT JOIN 
    village vl ON vl.address_id = p.addressid
WHERE 
    p.death = 'N'
    AND vl.village_code IS NOT NULL
    and p.birthday is not null
    AND p.pname IN ('นาย', 'นางสาว','นาง')
    AND p.addrpart REGEXP '[0-9]'
    AND LENGTH(YEAR(p.birthday)) = 4
GROUP BY 
    p.cid
