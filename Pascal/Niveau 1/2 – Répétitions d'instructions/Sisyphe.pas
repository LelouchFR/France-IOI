program Solution;
uses Robot;
var
   i: LongInt;
begin
   for i := 1 to 21 do
   begin
      haut;
      droite;
   end;
   for i := 1 to 21 do
   begin
      gauche;
      bas;
   end;
end.