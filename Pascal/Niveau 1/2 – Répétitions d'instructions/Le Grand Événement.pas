program Solution;
uses Robot;
var
   i: LongInt;
   j: LongInt;
begin
   haut();
   for i := 1 to 4 do
   begin
      for j := 1 to 8 do
      begin
         haut;
      end;
      droite;
      for j := 1 to 8 do
      begin
         bas;
      end;
      droite;
   end;
   for i := 1 to 8 do
   begin
      haut;
   end;
   droite;
   for i := 1 to 9 do
   begin
      bas;
   end;
   for i := 1 to 9 do
   begin
      gauche;
   end;
end.