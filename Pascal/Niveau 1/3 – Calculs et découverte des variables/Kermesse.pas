program Solution;
var
   bonbons, shots, i: LongInt;
begin
   bonbons := 0;
   shots := 1;
   for i := 1 to 50 do
   begin
      bonbons := bonbons + shots;
      writeln(bonbons);
      shots := shots + 1;
   end;
end.