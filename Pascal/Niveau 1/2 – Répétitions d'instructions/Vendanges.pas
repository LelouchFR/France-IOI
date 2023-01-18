program Solution;
uses robot;
var
   i: LongInt;
   j: LongInt;
begin
   for i := 1 to 20 do
   begin
      ramasser;
      for j := 1 to 15 do
      begin
         droite;
      end;
      deposer;
      for j := 1 to 15 do
      begin
         gauche;
      end;
   end;
end.