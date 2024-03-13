GET needs the in param for code and conditional WHERE:

PROCEDURE GET_FUNDING_TYPE_REF
   ( inSearchCode IN PAI.FUNDING_TYPE_REF%FTR_CODE
   refCursor IN OUT SYS_REFCURSOR ) IS

   SELECT blah blah
   FROM your table
   WHERE (inSearchCode IS NULL OR FTR_CODE = inSearchCode) 
