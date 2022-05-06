DECLARE 
  x NUMBER; 
  n NUMBER; 
  i NUMBER; 
    
  --function for finding sum 
  FUNCTION Findmax(n IN NUMBER) 
    RETURN NUMBER 
  IS 
    sums NUMBER := 0; 
  BEGIN 
    
    --for loop for n times iteration 
    FOR i IN 1..n 
    LOOP 
      sums := sums + i*(i+1)/2; 
    END LOOP; 
    RETURN sums; 
  END; 
  BEGIN 
    
    --driver code 
    n := 4; 
    x := findmax(n); 
    dbms_output.Put_line('Sum: ' 
    || x); 
  END;