program Solution;
uses Robot;
var
   i: integer;
begin
   for i := 1 to 3 do
   begin
      haut;
   end;
   for i := 1 to 2 do 
   begin
      droite;
   end;
   for i := 1 to 2 do
   begin   
      bas;
   end;
   droite;
end.