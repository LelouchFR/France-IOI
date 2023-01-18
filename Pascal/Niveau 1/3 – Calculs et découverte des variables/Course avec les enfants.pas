program Solution;
uses Robot;
var
   i, j, ring: LongInt;
begin
   ring := 1;
   for i := 1 to 10 do
   begin
      for j := 1 to ring do
      begin
         droite;
      end;
      ramasser;
      for j := 1 to ring do
      begin
         gauche;
      end;
      deposer;
      ring := ring + 1
   end;
end.