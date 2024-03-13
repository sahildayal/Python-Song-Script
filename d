GET needs the in param for code and conditional WHERE:

PROCEDURE GET_FUNDING_TYPE_REF
   ( inSearchCode IN PAI.FUNDING_TYPE_REF%FTR_CODE
   refCursor IN OUT SYS_REFCURSOR ) IS

   SELECT blah blah
   FROM your table
   WHERE (inSearchCode IS NULL OR FTR_CODE = inSearchCode) 


original
/************************************************************************************************
    Name:            GET_FUNDING_TYPE_REF

    Description:     This procedure retrieves data from the PAI.FUNDING_TYPE_REF table, which 
                     has information about funding types. 

    Author:          Sahil Dayal

    Date Created:    03/04/2024

 ************************************************************************************************/
PROCEDURE GET_FUNDING_TYPE_REF
   (refCursor IN OUT SYS_REFCURSOR) IS
BEGIN
    OPEN refCursor FOR
    SELECT FTR_CODE,   
           FTR_DESCRIPTION,   
           FTR_END_DATE,   
           FTR_CREATED_DATE,   
           FTR_CREATED_BY,   
           FTR_UPDATED_DATE,   
           FTR_UPDATED_BY
      FROM PAI.FUNDING_TYPE_REF;
    
    EXCEPTION
    WHEN NO_DATA_FOUND THEN
        NULL;
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20089, 'GET_FUNDING_TYPE_REF Error (' ||
                           TO_CHAR(SQLCODE) || ') - ' || (SQLERRM));
END GET_FUNDING_TYPE_REF;





updated:
/************************************************************************************************
    Name:            GET_FUNDING_TYPE_REF

    Description:     This procedure retrieves data from the PAI.FUNDING_TYPE_REF table, which 
                     has information about funding types. 

    Author:          Sahil Dayal

    Date Created:    03/04/2024

 ************************************************************************************************/
PROCEDURE GET_FUNDING_TYPE_REF
   (inSearchCode IN VARCHAR2,
    refCursor IN OUT SYS_REFCURSOR) IS
BEGIN
    OPEN refCursor FOR
    SELECT FTR_CODE,   
           FTR_DESCRIPTION,   
           FTR_END_DATE,   
           FTR_CREATED_DATE,   
           FTR_CREATED_BY,   
           FTR_UPDATED_DATE,   
           FTR_UPDATED_BY
      FROM PAI.FUNDING_TYPE_REF
     WHERE (inSearchCode IS NULL OR FTR_CODE = inSearchCode);
    
    EXCEPTION
    WHEN NO_DATA_FOUND THEN
        NULL;
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20089, 'GET_FUNDING_TYPE_REF Error (' ||
                           TO_CHAR(SQLCODE) || ') - ' || (SQLERRM));
END GET_FUNDING_TYPE_REF;

