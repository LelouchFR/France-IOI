program Solution;
uses Robot;
var
   i: LongInt;
   j: LongInt;
begin
   for i := 1 to 108 do
   begin
      for j := 1 to 13 do
      begin
         haut;
      end;
      for j:= 1 to 13 do
      begin
         droite;
      end;
      for j:= 1 to 13 do
      begin
         bas;
      end;
      for j:= 1 to 13 do
      begin
         gauche;
      end;
   end;
end.