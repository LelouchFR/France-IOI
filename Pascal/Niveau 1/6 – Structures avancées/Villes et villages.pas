program Solution;
var
   area, city, i, pop: LongInt;
begin
   read(area);
   city := 0;
   for i := 1 to area do
   begin
      read(pop);
      if pop > 10 * 1000 then
      begin
         city := city + 1;
      end;
   end;
   writeln(city);
end.