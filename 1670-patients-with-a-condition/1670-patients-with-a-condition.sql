-- Retrieve patient records where the condition includes 'DIAB1' at the beginning or in the middle of the string
SELECT 
    patient_id,                -- Select the patient's ID
    patient_name,              -- Select the patient's name
    conditions                 -- Select the patient's medical conditions
FROM 
    Patients                   -- Specify the table containing the patient data
WHERE 
    conditions LIKE 'DIAB1%'   -- Match conditions that start with 'DIAB1'
    OR conditions LIKE '% DIAB1%'; -- Match conditions that include 'DIAB1' as a separate word
