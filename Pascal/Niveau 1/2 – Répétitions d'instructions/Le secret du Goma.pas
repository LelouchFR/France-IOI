program Solution;
uses Robot;
var
   i: LongInt;
begin
   for i := 1 to 15 do
   begin
      droite;
      ramasser;
   end;
   droite;
   deposer;
end.